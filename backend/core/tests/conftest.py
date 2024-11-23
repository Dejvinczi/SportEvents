import pytest
from django.utils import timezone
from ..models import User, Event


@pytest.fixture()
def user_data():
    return {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "testuserpass",
    }


@pytest.fixture()
def user(user_data):
    return User.objects.create_user(**user_data)


@pytest.fixture
def event_data():
    return {
        "name": "testevent",
        "start_at": timezone.now() + timezone.timedelta(days=7),
        "location": "testlocation",
        "participant_limit": 10,
        "description": "testdescription",
    }


@pytest.fixture
def event(event_data):
    return Event.objects.create(**event_data)
