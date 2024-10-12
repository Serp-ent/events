from . import views
from django.urls import path

app_name = "events"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:event_id>/", views.event_detail, name="detailed_event"),
]
