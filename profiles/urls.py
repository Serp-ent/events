from django.urls import path, include
from . import views

# Create your views here.

# TODO: how to keep layout across all apps

urlpatterns = [
  path('<int:user_id>/', views.profile_detail),
  path('edit/', views.profile_edit),
]