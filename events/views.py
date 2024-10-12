from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.urls import reverse

from .models import Event


# Create your views here.
def index(request):
    events = Event.objects.all()

    return render(request, "events/index.html", {"events_list": events})


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    return render(request, "events/event.html", {"event": event})


def join_event(request, event_id):
    # TODO: join event
    return HttpResponseRedirect(reverse("events:detailed_event", args=[event_id]))


def create_event(request: HttpRequest):
    return HttpResponse("TODO: show form for event creation")


def remove_event(request: HttpRequest, event_id):
    return HttpResponse(f"TODO: remove item with id {event_id}")


def edit_event(request: HttpRequest, event_id):
    return HttpResponse(f"TODO: edit item with id {event_id}")
