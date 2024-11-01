from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm


def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()

    context = {"form": form}

    return render(request, "events/register.html", context)


def MyLogin(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print(user)
            login(request, user)
            return redirect(reverse("events:index"))
    else:
        form = AuthenticationForm()

    context = {"form": form}
    return render(request, "events/login.html", context)
