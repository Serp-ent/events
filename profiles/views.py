from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile
from .forms import ProfileForm
from django.http import HttpResponse, HttpRequest

# TODO: login required


def profile_detail(request: HttpRequest, user_id: int) -> HttpResponse:
    profile: Profile = get_object_or_404(Profile, user_id=user_id)
    return render(request, "profiles/profile_detail.html", {"profile": profile})


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
