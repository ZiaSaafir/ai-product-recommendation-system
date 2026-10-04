from rest_framework import permissions
from rest_framework import viewsets

from .models import UserInteraction
from .serializers import UserInteractionSerializer


class UserInteractionViewSet(viewsets.ModelViewSet):

    serializer_class = UserInteractionSerializer

    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get_queryset(self):
        return (
            UserInteraction.objects
            .filter(user=self.request.user)
            .select_related("product")
        )

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )