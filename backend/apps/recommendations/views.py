
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .engine import get_recommendations
from .serializers import RecommendationSerializer


class RecommendationView(APIView):

    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get(self, request):

        # Get recommendations from ML engine
        recommendations = get_recommendations(
            user=request.user,
            limit=5,
        )

        # Extract Product objects
        products = [
            item["product"]
            for item in recommendations
        ]

        # Serialize Product objects
        serializer = RecommendationSerializer(
            products,
            many=True,
        )

        # Add recommendation score
        results = []

        for item, serialized_product in zip(
            recommendations,
            serializer.data,
        ):
            results.append({
                **serialized_product,
                "recommendation_score": item["score"],
            })

        return Response({
            "count": len(results),
            "results": results,
        })
