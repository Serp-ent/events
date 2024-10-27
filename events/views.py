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
    paginate_by = 5


class EventDetailView(generic.DetailView):
    model = Event
    template_name = "events/event.html"


def join_event(request, event_id):
    # TODO: join event
    return HttpResponseRedirect(reverse("events:detailed_event", args=[event_id]))


def create_event(request: HttpRequest):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
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
