from django.urls import path
from .views import SignUpView
from .views import (
    UpdateCityView,
    UpdateCity2View,
    UpdateCity3View,
    UpdateCity4View,
    UpdateCity5View,
)

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("update_city/", UpdateCityView.as_view(), name="update_city"),
    path("update_city2/", UpdateCity2View.as_view(), name="update_city2"),
    path("update_city3/", UpdateCity3View.as_view(), name="update_city3"),
    path("update_city4/", UpdateCity4View.as_view(), name="update_city4"),
    path("update_city5/", UpdateCity5View.as_view(), name="update_city5"),
]
