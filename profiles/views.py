from django.shortcuts import render, get_object_or_404
from .models import Profile
from django.http import HttpResponse, HttpRequest

# TODO: login required

def profile_detail(request: HttpRequest, user_id: int) -> HttpResponse:
    profile: Profile = get_object_or_404(Profile, user_id=user_id)
    return render(request, "profiles/profile_detail.html", {"profile": profile})


def profile_edit(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Edit profile")
