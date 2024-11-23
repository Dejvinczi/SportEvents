import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestUserViewSet:

    LIST_URL = reverse("core:users-list")

    def test_create(self, api_client, user_model):
        payload = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testuserpass",
        }

        res = api_client.post(self.LIST_URL, payload, format="json")

        assert res.status_code == 201
        assert "password" not in res.data
        assert res.data["username"] == payload["username"]
        assert res.data["email"] == payload["email"]
        assert user_model.objects.filter(username=payload["username"]).exists()
