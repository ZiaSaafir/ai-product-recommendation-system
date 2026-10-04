from django.contrib import admin
from django.urls import include, path

# http:127:8000/api/product
urlpatterns = [
    path("admin/", admin.site.urls),

    path(
        "api/auth/",
        include("apps.accounts.urls"),
    ),

    path(
        "api/",
        include("apps.products.urls"),
    ),
    path(
    "api/recommendations/",
    include("apps.recommendations.urls")
    ),

    path(
        "api/",
        include("apps.interactions.urls"),
    ),
]