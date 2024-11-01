from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    avatar = models.ImageField(upload_to="profile_pictures/", blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.user.username}'s Profile"
