from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializers import ProductSerializer
from .models import Product


class ProductViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = ProductSerializer

    permission_classes = [AllowAny]

    search_fields = [
        "name",
        "description",
        "brand__name",
        "category__name",
    ]

    def get_queryset(self):

        return (
            Product.objects
            .filter(is_active=True)
            .select_related(
                "category",
                "brand"
            )
            .order_by("-created_at")
        )
