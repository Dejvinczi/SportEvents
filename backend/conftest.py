import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient


@pytest.fixture
def user_model():
    return get_user_model()


@pytest.fixture()
def api_client():
    yield APIClient()
