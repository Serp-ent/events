from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from django.contrib.auth.models import User
from events.models import Event
from .forms import ProfileForm
from django.http import HttpResponse, HttpRequest

# TODO: login required


def profile_detail(request: HttpRequest, user_id: int) -> HttpResponse:
    profile: Profile = get_object_or_404(Profile, user_id=user_id)
    return render(request, "profiles/profile_detail.html", {"profile": profile})


def events_created(request: HttpRequest, user_id: int) -> HttpResponse:
    user: User = get_object_or_404(User, id=user_id)
    events = Event.objects.filter(author=user)

    # TODO: maybe in template add avatar
    return render(
        request,
        "events/events_created.html",
        {
            "user": user,
            "events": events,
        },
    )


def events_joined(request: HttpRequest, user_id: int) -> HttpResponse:
    user: User = get_object_or_404(User, id=user_id)
    events = user.registrations.all()

    return render(
        request,
        "events/events_joined.html",
        {
            "user": user,
            "events": events,
        },
    )


# TODO: login required
def profile_edit(request: HttpRequest) -> HttpResponse:
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profiles:profile_detail", user_id=request.user.id)
    else:
        form = ProfileForm(instance=profile)

    context = {"form": form}
    return render(request, "profiles/edit_profile.html", context)
