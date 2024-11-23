import pytest
from django.utils import timezone
from ..models import User, Event, EventParticipant


@pytest.mark.django_db
class TestUserModel:
    """User model tests."""

    def test_create_user(self, user_data):
        """Test creation new user instance."""
        user = User.objects.create_user(**user_data)

        assert user.id is not None
        assert user.username == user_data["username"]
        assert user.email == user_data["email"]
        assert user.check_password(user_data["password"])


@pytest.mark.django_db
class TestEventModel:
    """Event model tests."""

    def test_create(self, event_data):
        """Test creation new event instace."""
        event = Event.objects.create(**event_data)

        assert event.id is not None
        assert event.name == event_data["name"]
        assert event.start_at == event_data["start_at"]
        assert event.location == event_data["location"]
        assert event.participant_limit == event_data["participant_limit"]
        assert event.description == event_data["description"]

    def test_default_status(self, event):
        """Test default event status."""
        assert event.status == Event.Status.PLANNED

    def test_string_representation(self, event):
        """Test string representation event instance"""
        assert str(event) == f"{event.name}({event.start_at}) - {event.status}"


@pytest.mark.django_db
class TestEventParticipiant:
    """EventParticipiant model tests."""

    def test_create(self, event, user):
        """Test creation of new event participiant instance."""
        event_paricipant = EventParticipant.objects.create(event=event, user=user)

        assert event_paricipant.event == event
        assert event_paricipant.user == user
        assert event_paricipant.joined_at is not None
        assert event_paricipant.joined_at < timezone.now()
