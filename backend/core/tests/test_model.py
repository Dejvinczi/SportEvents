import pytest
from ..models import User


@pytest.mark.django_db
class TestUserModel:
    """User model tests."""

    def test_create_user(self):
        """Test creation new user instance."""
        user_data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testuserpass",
        }
        user = User.objects.create_user(**user_data)

        assert user.id is not None
        assert user.username == user_data["username"]
        assert user.email == user_data["email"]
        assert user.check_password(user_data["password"])
