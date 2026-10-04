
import { useEffect, useState } from "react";
import { Link, useParams } from "react-router-dom";

import "../css/ProductDetail.css";
import { getAccessToken } from "../services/api";


function ProductDetail() {

    // Get product ID from URL
    const { id } = useParams();

    const [product, setProduct] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState("");


    // =========================
    // LOAD PRODUCT
    // =========================

    useEffect(() => {

        async function loadProduct() {

            try {

                const response = await fetch(
                    `http://127.0.0.1:8000/api/products/${id}/`
                );

                if (!response.ok) {
                    throw new Error(
                        "Could not load product."
                    );
                }

                const data = await response.json();

                setProduct(data);

            } catch (error) {

                console.error(
                    "Product detail error:",
                    error
                );

                setError(
                    error.message ||
                    "Something went wrong."
                );

            } finally {

                setLoading(false);
            }
        }

        loadProduct();

    }, [id]);


    // =========================
    // RECORD INTERACTION
    // =========================

    async function recordInteraction(
        interactionType,
        successMessage
    ) {

        const token = getAccessToken();

        // User is not logged in
        if (!token) {

            alert(
                "Please login to record your interaction."
            );

            return;
        }

        try {

            const response = await fetch(
                "http://127.0.0.1:8000/api/interactions/",
                {
                    method: "POST",

                    headers: {
                        "Content-Type": "application/json",
                        "Authorization": `Bearer ${token}`,
                    },

                    body: JSON.stringify({
                        product: Number(id),
                        interaction_type: interactionType,
                    }),
                }
            );


            if (!response.ok) {

                console.error(
                    `Could not record ${interactionType} interaction.`
                );

                return;
            }


            const data = await response.json();


            console.log(
                `${interactionType} interaction recorded:`,
                data
            );


            if (successMessage) {
                alert(successMessage);
            }


        } catch (error) {

            console.error(
                `${interactionType} interaction error:`,
                error
            );
        }
    }


    // =========================
    // RECORD PRODUCT VIEW
    // =========================

    useEffect(() => {

        async function recordView() {

            const token = getAccessToken();

            // Don't record views for guests
            if (!token) {
                return;
            }

            await recordInteraction(
                "VIEW",
                null
            );
        }

        recordView();

    }, [id]);


    // =========================
    // LIKE PRODUCT
    // =========================

    function handleLike() {

        recordInteraction(
            "LIKE",
            "❤️ Product liked!"
        );
    }


    // =========================
    // ADD TO CART
    // =========================

    function handleCart() {

        recordInteraction(
            "CART",
            "🛒 Product added to cart!"
        );
    }


    // =========================
    // PURCHASE PRODUCT
    // =========================

    function handlePurchase() {

        recordInteraction(
            "PURCHASE",
            "🎉 Purchase recorded!"
        );
    }


    // =========================
    // LOADING
    // =========================

    if (loading) {

        return (

            <div className="loading-page">

                <div className="loader"></div>

                <p>
                    Loading product...
                </p>

            </div>
        );
    }


    // =========================
    // ERROR
    // =========================

    if (error) {

        return (

            <div className="error-page">

                <h2>
                    Product Not Found
                </h2>

                <p>
                    {error}
                </p>

                <Link
                    to="/"
                    className="primary-button"
                >
                    Back to Home
                </Link>

            </div>
        );
    }


    // =========================
    // PRODUCT DETAIL
    // =========================

    return (

        <div className="product-detail-page">


            {/* NAVBAR */}

            <header className="navbar">

                <Link
                    to="/"
                    className="logo"
                >
                    AI<span>Recommend</span>
                </Link>


                <Link
                    to="/"
                    className="back-link"
                >
                    ← Back to Products
                </Link>

            </header>


            {/* PRODUCT DETAIL */}

            <main className="product-detail">


                {/* PRODUCT IMAGE */}

                <div className="product-detail-image">

                    {product.image ? (

                        <img
                            src={product.image}
                            alt={product.name}
                        />

                    ) : (

                        <span>
                            No Image Available
                        </span>

                    )}

                </div>


                {/* PRODUCT INFORMATION */}

                <div className="product-detail-info">


                    {/* CATEGORY */}

                    <span className="category">

                        {
                            product.category?.name ||
                            "Product"
                        }

                    </span>


                    {/* NAME */}

                    <h1>
                        {product.name}
                    </h1>


                    {/* DESCRIPTION */}

                    <p className="product-description">

                        {
                            product.description ||
                            "No description available."
                        }

                    </p>


                    {/* PRICE */}

                    <div className="detail-price">

                        ${product.price}

                    </div>


                    {/* ACTION BUTTONS */}

                    <div className="product-actions">

                        <button
                            className="primary-button"
                            onClick={handleLike}
                        >
                            ♡ Like Product
                        </button>


                        <button
                            className="secondary-button"
                            onClick={handleCart}
                        >
                            🛒 Add to Cart
                        </button>


                        <button
                            className="primary-button"
                            onClick={handlePurchase}
                        >
                            💰 Buy Now
                        </button>

                    </div>


                    {/* RECOMMENDATION MESSAGE */}

                    <p className="recommendation-note">

                        AI Recommend will use your
                        product interactions to
                        improve future recommendations.

                    </p>

                </div>

            </main>

        </div>
    );
}


export default ProductDetail;