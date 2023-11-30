from django.urls import path
from .views import SignUpView
from .views import UpdateCityView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("update_city/", UpdateCityView.as_view(), name="update_city"),
]
