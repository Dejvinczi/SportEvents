from . import views
from django.urls import path
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

router = DefaultRouter()
router.register("users", views.UserViewSet, basename="users")

app_name = "core"

urlpatterns = [
    path("schema", SpectacularAPIView.as_view(), name="schema"),
    path(
        "schema/swagger-ui",
        SpectacularSwaggerView.as_view(url_name="core:schema"),
        name="schema_swagger-ui",
    ),
    path(
        "schema/redoc",
        SpectacularRedocView.as_view(url_name="core:schema"),
        name="schema_redoc",
    ),
    path("token", views.CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", views.CustomTokenRefreshView.as_view(), name="token_refesh"),
]


urlpatterns += router.urls
