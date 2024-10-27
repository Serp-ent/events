from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# TODO: login required


def profile_detail(request: HttpRequest, user_id: int) -> HttpResponse:
    return HttpResponse("Display profile detail")


def profile_edit(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Edit profile")
