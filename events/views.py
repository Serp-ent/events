from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.urls import reverse
from .forms import EventForm

from django.views import generic

from .models import Event


class EventListView(generic.ListView):
    template_name = "events/index.html"
    model = Event
    context_object_name = "events_list"


class EventDetailView(generic.DetailView):
    model = Event
    template_name = "events/event.html"


def join_event(request, event_id):
    # TODO: join event
    return HttpResponseRedirect(reverse("events:detailed_event", args=[event_id]))


def create_event(request: HttpRequest):
    if request.method == "POST":
        print("Received POST request create_event")
        form = EventForm(request.POST)  # this is called binding data to the form
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/events")
    else:
        form = EventForm()

    context = {"form": form}

    return render(request, "events/create_event.html", context)


def remove_event(request: HttpRequest, event_id):
    return HttpResponse(f"TODO: remove item with id {event_id}")


def edit_event(request: HttpRequest, event_id):
    return HttpResponse(f"TODO: edit item with id {event_id}")
