from rest_framework import serializers
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """User model serializer."""

    class Meta:
        model = User
        fields = ("username", "password", "email")
        extra_kwargs = {"password": {"write_only": True}, "email": {"required": True}}

    def create(self, validated_data):
        return self.Meta.model.objects.create_user(**validated_data)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Custom class for obtaining pair of tokens."""

    pass


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    """Custom class for refreshing token."""

    pass
