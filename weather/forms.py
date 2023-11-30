from django.forms import ModelForm
from .models import City


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ["name"]
        widgets = {
            "name": forms.TextInput(
                attrs={"class": "input", "placeholder": "City Name"}
            )
        }
