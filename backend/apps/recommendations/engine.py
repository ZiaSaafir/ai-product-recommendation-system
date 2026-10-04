from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from apps.interactions.models import UserInteraction
from apps.products.models import Product


INTERACTION_WEIGHTS = {
    "VIEW": 1,
    "CLICK": 2,
    "LIKE": 3,
    "CART": 4,
    "PURCHASE": 5,
}


def get_recommendations(user, limit=5):
    """
    V2.1 Recommendation Engine

    Uses:
    - User interactions
    - Interaction weights
    - Product text
    - TF-IDF
    - Cosine similarity
    - Normalized recommendation scores

    Returns:
    [
        {
            "product": Product object,
            "score": float,
        }
    ]
    """

    # --------------------------------------------------
    # 1. Get user's interaction history
    # --------------------------------------------------

    interactions = (
        UserInteraction.objects
        .filter(user=user)
        .select_related(
            "product",
            "product__category",
            "product__brand",
        )
        .order_by("-created_at")
    )

    # --------------------------------------------------
    # 2. Assign interaction weights
    # --------------------------------------------------

    product_weights = {}

    for interaction in interactions:

        product_id = interaction.product_id

        weight = INTERACTION_WEIGHTS.get(
            interaction.interaction_type,
            1,
        )

        # Keep the strongest interaction
        # for each product.
        if (
            product_id not in product_weights
            or weight > product_weights[product_id]["weight"]
        ):
            product_weights[product_id] = {
                "product": interaction.product,
                "weight": weight,
            }

    # --------------------------------------------------
    # 3. Get products the user interacted with
    # --------------------------------------------------

    interacted_products = [
        item["product"]
        for item in product_weights.values()
    ]

    # --------------------------------------------------
    # 4. Cold-start fallback
    # --------------------------------------------------

    if not interacted_products:

        products = (
            Product.objects
            .filter(is_active=True)
            .select_related(
                "category",
                "brand",
            )
            .order_by("-created_at")[:limit]
        )

        return [
            {
                "product": product,
                "score": 0.0,
            }
            for product in products
        ]

    # --------------------------------------------------
    # 5. Get all active products
    # --------------------------------------------------

    products = list(
        Product.objects
        .filter(is_active=True)
        .select_related(
            "category",
            "brand",
        )
    )

    interacted_ids = set(
        product_weights.keys()
    )

    # --------------------------------------------------
    # 6. Remove already interacted products
    # --------------------------------------------------

    candidate_products = [
        product
        for product in products
        if product.id not in interacted_ids
    ]

    # --------------------------------------------------
    # 7. If there are no candidates
    # --------------------------------------------------

    if not candidate_products:

        return [
            {
                "product": product,
                "score": 0.0,
            }
            for product in products[:limit]
        ]

    # --------------------------------------------------
    # 8. Create searchable product text
    # --------------------------------------------------

    def product_text(product):

        category = (
            product.category.name
            if product.category
            else ""
        )

        brand = (
            product.brand.name
            if product.brand
            else ""
        )

        return " ".join([
            product.name or "",
            product.description or "",
            category,
            brand,
        ])

    # --------------------------------------------------
    # 9. Combine interacted + candidate products
    # --------------------------------------------------

    all_products = (
        interacted_products
        + candidate_products
    )

    product_texts = [
        product_text(product)
        for product in all_products
    ]

    # --------------------------------------------------
    # 10. Convert product text into TF-IDF vectors
    # --------------------------------------------------

    vectorizer = TfidfVectorizer(
        stop_words="english"
    )

    tfidf_matrix = vectorizer.fit_transform(
        product_texts
    )

    # --------------------------------------------------
    # 11. Calculate cosine similarity
    # --------------------------------------------------

    similarity_matrix = cosine_similarity(
        tfidf_matrix
    )

    interacted_count = len(
        interacted_products
    )

    # --------------------------------------------------
    # 12. Calculate recommendation scores
    # --------------------------------------------------

    scored_products = []

    for candidate_index in range(
        interacted_count,
        len(all_products),
    ):

        weighted_scores = []

        for user_index in range(
            interacted_count
        ):

            interacted_product = (
                interacted_products[user_index]
            )

            interaction_weight = (
                product_weights[
                    interacted_product.id
                ]["weight"]
            )

            similarity = similarity_matrix[
                candidate_index
            ][user_index]

            weighted_score = (
                similarity
                * interaction_weight
            )

            weighted_scores.append(
                weighted_score
            )

        if weighted_scores:

            final_score = max(
                weighted_scores
            )

        else:

            final_score = 0.0

        candidate_product = (
            candidate_products[
                candidate_index
                - interacted_count
            ]
        )

        scored_products.append({
            "product": candidate_product,
            "score": float(final_score),
        })

    # --------------------------------------------------
    # 13. Sort by recommendation score
    # --------------------------------------------------

    scored_products.sort(
        key=lambda item: item["score"],
        reverse=True,
    )

    # --------------------------------------------------
    # 14. Normalize scores to 0–100
    # --------------------------------------------------

    if scored_products:

        max_score = scored_products[0]["score"]

        if max_score > 0:

            for item in scored_products:

                item["score"] = round(
                    (
                        item["score"]
                        / max_score
                    ) * 100,
                    2,
                )

        else:

            for item in scored_products:
                item["score"] = 0.0

    # --------------------------------------------------
    # 15. Return top recommendations
    # --------------------------------------------------

    return scored_products[:limit]