from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.urls import reverse
from .forms import EventForm
from django.contrib import messages
from django.contrib.auth.models import User

from django.views import generic

from .models import Event, EventRegistration


class EventListView(generic.ListView):
    template_name = "events/index.html"
    model = Event
    context_object_name = "events_list"
    paginate_by = 5

    def get_queryset(self) -> QuerySet[Event]:
        events: QuerySet[Event] = super().get_queryset()
        user: User = self.request.user
        for event in events:
            event.is_registered = (
                event.is_user_registered(user) if user.is_authenticated else False
            )
        return events


class EventDetailView(generic.DetailView):
    model = Event
    template_name = "events/event.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        user: User = self.request.user
        event: Event = self.get_object()

        context["is_registered"] = (
            event.is_user_registered(user) if user.is_authenticated else False
        )

        return context


def join_event(request: HttpRequest, event_id: int) -> HttpResponse:
    event = get_object_or_404(Event, id=event_id)
    # Check if the event is not full
    # TODO: the model should have method for that
    # INFO: Thick models slim views
    if EventRegistration.objects.filter(user=request.user, event=event).exists():
        messages.info(request, "You are already registered for this event")
    elif (
        event.participant_limit > 0
        and event.registrations.count() >= event.participant_limit
    ):
        messages.error(request, "Sorry, this event is already full.")
    else:
        EventRegistration.objects.create(user=request.user, event=event)
    return redirect("events:detailed_event", pk=event.id)


def leave_event(request: HttpRequest, event_id: int) -> HttpResponse:
    event = get_object_or_404(Event, id=event_id)
    registration = EventRegistration.objects.filter(event=event, user=request.user)
    if registration == None:
        messages.error(request, "You are not registered for this event.")
    else:
        registration.delete()
        messages.success(request, "You have left the event.")

    return redirect("events:detailed_event", pk=event_id)


# TODO: login_required
def create_event(request: HttpRequest):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event: Event = form.save(commit=False)
            event.author = request.user
            event.save()

            return HttpResponseRedirect("/events")
        else:
            print(form.errors)
    else:
        form = EventForm()

    context = {"form": form}

    return render(request, "events/create_event.html", context)


def remove_event(request: HttpRequest, event_id: str) -> HttpResponse:
    e = get_object_or_404(Event, pk=event_id)
    e.delete()

    return HttpResponseRedirect(reverse("events:index"))


def edit_event(request: HttpRequest, event_id: str):
    e = get_object_or_404(Event, pk=event_id)

    if request.method == "POST":
        form = EventForm(request.POST, instance=e)
        if form.is_valid():
            form.save()
            # TODO: this should redirect to that event using reverse
            return HttpResponseRedirect("/events")
    else:
        form = EventForm(instance=e)

    context = {"form": form, "event": e}
    return render(request, "events/edit_event.html", context)
