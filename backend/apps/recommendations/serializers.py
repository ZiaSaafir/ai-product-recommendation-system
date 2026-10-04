from rest_framework import serializers

from apps.products.models import Product


class RecommendationSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(
        source="category.name",
        read_only=True,
    )

    brand_name = serializers.CharField(
        source="brand.name",
        read_only=True,
    )

    class Meta:
        model = Product

        fields = [
            "id",
            "name",
            "description",
            "price",
            "image",
            "category",
            "category_name",
            "brand",
            "brand_name",
        ]