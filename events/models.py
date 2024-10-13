from django.db import models
from django.contrib.auth.models import AbstractUser


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

    def __str__(self) -> str:
        return self.name


# class EventRegistration(models.Model):
