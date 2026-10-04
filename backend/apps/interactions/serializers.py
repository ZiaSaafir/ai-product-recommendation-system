from rest_framework import serializers

from .models import UserInteraction


class UserInteractionSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserInteraction

        fields = [
            "id",
            "product",
            "interaction_type",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]