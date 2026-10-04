from django.conf import settings
from django.db import models


class UserInteraction(models.Model):

    class InteractionType(models.TextChoices):
        VIEW = "VIEW", "View"
        CLICK = "CLICK", "Click"
        LIKE = "LIKE", "Like"
        CART = "CART", "Cart"
        PURCHASE = "PURCHASE", "Purchase"

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="interactions",
    )

    product = models.ForeignKey(
        "products.Product",
        on_delete=models.CASCADE,
        related_name="interactions",
    )

    interaction_type = models.CharField(
        max_length=20,
        choices=InteractionType.choices,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user.username} - "
            f"{self.product.name} - "
            f"{self.interaction_type}"
        )