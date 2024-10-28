from django.urls import path, include
from . import views

# Create your views here.

# TODO: how to keep layout across all apps

app_name = "profiles"

urlpatterns = [
    # TODO: user own profile detail
    path("<int:user_id>/", views.profile_detail, name="profile_detail"),
    path("edit/", views.profile_edit),
]
