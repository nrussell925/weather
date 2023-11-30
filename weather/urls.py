from django.urls import path
from . import views
from .views import SignUpView, UpdateCityView

urlpatterns = [
    path("", views.home),  # home view, is essentially our "home page"
    path("signup/", SignUpView.as_view(), name="signup"),
    path("update_city/", UpdateCityView.as_view(), name="update_city"),
]
