from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            "age",
            "city",  # all cities will need a different name
            "city2",
            "city3",
            "city4",
            "city5",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class SearchForm(
    forms.Form
):  # user types city into search bar and it's added to their account
    query = forms.CharField(label="Search", max_length=100)
