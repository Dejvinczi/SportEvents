from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """User database representation model."""

    pass


class Event(models.Model):
    """Event database representation model."""

    class Status(models.TextChoices):
        PLANNED = "planned", "Planned"
        IN_PROGRESS = "in_progress", "In Progress"
        COMPLETED = "completed", "Completed"

    name = models.CharField(max_length=255)
    start_at = models.DateTimeField()
    location = models.TextField()
    participant_limit = models.PositiveBigIntegerField()
    description = models.TextField(blank=True)
    status = models.CharField(
        max_length=11, choices=Status.choices, default=Status.PLANNED
    )
    participants = models.ManyToManyField(to=User, through="EventParticipant")

    def __str__(self):
        return f"{self.name}({self.start_at}) - {self.status}"


class EventParticipant(models.Model):
    """Event participant representation model."""

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
