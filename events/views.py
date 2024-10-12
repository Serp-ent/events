from django.shortcuts import render
from django.http import HttpResponse

from .models import Event


# Create your views here.
def index(request):
    events = Event.objects.all()

    return HttpResponse(events)


def event_detail(request, event_id):
    return HttpResponse(f"Event detail for {event_id}")
