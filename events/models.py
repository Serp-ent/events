from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()

    photo = models.ImageField(upload_to="event_photos/", null=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="events")
    participant_limit = models.PositiveIntegerField(default=0)

    def is_user_registered(self, user) -> bool:
        if user.is_authenticated:
            return self.registrations.filter(user=user).exists()

        return False

    def available_slots(self):
        if self.participant_limit > 0:
            return self.participant_limit - self.registrations.count()
        return None

    def __str__(self) -> str:
        return self.name


class EventRegistration(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="registrations"
    )
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="registrations"
    )

    class Meta:
        unique_together = ("user", "event")

    def __str__(self) -> str:
        return f"{self.user.username} registered for {self.event.name}"
