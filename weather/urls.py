from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),  # home view, is essentially our "home page"
]
