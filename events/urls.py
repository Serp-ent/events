from . import views
from django.urls import path

app_name = "events"

# TODO:
# Organizers can create events with details such as:

#     Event name
#     Date and time
#     Location (physical or virtual)
#     Description
#     Maximum number of participants
#     Optional cover image for the event

# Organizers can update or delete their own events.

# TODO:
# Participants can browse upcoming events by:

#     Category (e.g., Music, Technology, Education, etc.)
#     Date and time
#     Location (with a filter for nearby events)

# Search functionality for events based on keywords.
# Pagination for event listings.

# TODO:
# Participants can register for events.
# Event capacity management: Events can have a limited number of spots, and participants are prevented from registering once the event is full.
# Registration confirmation email sent to participants.

# TODO:
# User Dashboards:

#     Organizer Dashboard:
#         View all created events.
#         See the list of participants who have registered for each event.
#         Option to download a CSV of all registered participants.
#     Participant Dashboard:
#         View upcoming events they have registered for.
#         Cancel registration for any event before the event starts.

urlpatterns = [
    path("", views.EventListView.as_view(), name="index"),
    path("<int:pk>/", views.EventDetailView.as_view(), name="detailed_event"),
    path("<int:event_id>/join", views.join_event, name="join_event"),
    path("new/", views.create_event, name="create_event"),
    path("<int:event_id>/remove", views.remove_event, name="remove_event"),
    path("<int:event_id>/edit", views.edit_event, name="edit_event"),
]

