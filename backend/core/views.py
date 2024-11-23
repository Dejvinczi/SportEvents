from rest_framework import viewsets, mixins
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializers import (
    CustomTokenObtainPairSerializer,
    CustomTokenRefreshSerializer,
    UserSerializer,
)


class UserViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """API view sets for managing users."""

    serializer_class = UserSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    """Custom view class for obtaining token pair."""

    serializer_class = CustomTokenObtainPairSerializer


class CustomTokenRefreshView(TokenRefreshView):
    """Custom view class for refresh token."""

    serializer_class = CustomTokenRefreshSerializer
