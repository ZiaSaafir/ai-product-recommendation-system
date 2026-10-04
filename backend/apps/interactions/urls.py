from rest_framework.routers import DefaultRouter

from .views import UserInteractionViewSet


router = DefaultRouter()

router.register(
    "interactions",
    UserInteractionViewSet,
    basename="interaction",
)

urlpatterns = router.urls