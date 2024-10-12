from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Event


# Create your views here.
def index(request):
    events = Event.objects.all()

    return render(request, "events/index.html", {"events_list": events})


def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    return HttpResponse(f"Event detail for {event_id}")
