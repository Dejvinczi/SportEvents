from . import views
from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("users", views.UserViewSet, basename="users")

app_name = "core"

urlpatterns = [
    path("token", views.CustomTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path(
        "token/refresh",
        views.CustomTokenRefreshView.as_view(),
        name="token_refesh",
    ),
]


urlpatterns += router.urls
