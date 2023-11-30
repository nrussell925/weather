from .forms import CustomUserCreationForm, SearchForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import View
from django.shortcuts import render, redirect


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class UpdateCityView(View):
    template_name = "update_city.html"

    def get(self, request):
        form = SearchForm()
        return render(request, "update_city.html", {"form": form})

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data["query"]
            request.user.city = city
            request.user.save()
            return redirect("home")
        return render(request, "update_city.html", {"form": form})
