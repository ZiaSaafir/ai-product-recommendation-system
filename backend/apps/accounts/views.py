from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializer


class HealthCheckView(APIView):
    permission_classes = [
        permissions.AllowAny,
    ]

    def get(self, request):
        return Response(
            {
                "status": "success",
                "message": "AI Recommendation API is running.",
            }
        )


class CurrentUserView(APIView):
    permission_classes = [
        permissions.IsAuthenticated,
    ]

    def get(self, request):
        serializer = UserSerializer(
            request.user
        )

        return Response(
            serializer.data
        )

from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):

    serializer_class = RegisterSerializer

    permission_classes = [
        AllowAny,
    ]
    