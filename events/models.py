from django.db import models


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

    def __str__(self) -> str:
        return self.name


# class EventRegistration(models.Model):
