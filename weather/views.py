from django.shortcuts import render


def home(request):
    return render(
        request,
        "home.html",
    )  # home.html currently has "city temperatures"; is currently static and not using API
