from django.db import models
from django.contrib.auth.models import User


# TODO: add roles organizer and participant
# TODO: add login/register and logout functionality


# Create your models here.
class Event(models.Model):
    # TODO: this should be other model
    CATEGORY_CHOICES = [
        ("music", "Music"),
        ("technology", "Technology"),
        ("education", "Education"),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    startAt = models.DateTimeField()
    # TODO: endsAt = models.DateTimeField()
    photo = models.ImageField(upload_to="event_photos/", null=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")

    def __str__(self) -> str:
        return self.name


# class EventRegistration(models.Model):
