from django.shortcuts import render
import requests


def home(request):
    city = "Missoula"
    api_url = f"https://api.weather.gov/points/{46.8721}, {113.9940}"  # lat and long for Missoula; just for testing
    response_metadata = requests.get(api_url)

    data_metadata = response_metadata.json()
    forecast_url = data_metadata["properties"]["forecast"]

    response_forecast = requests.get(forecast_url)
    response_weather = requests.get(api_url).json()
    data_forecast = response_forecast.json()

    temperature = data_forecast["properties"]["periods"][0]["temperature"]
    description = data_forecast["properties"]["periods"][0]["shortForecast"]
    city_2 = data_forecast["properties"]["relativeLocation"]["properties"]["city"]
    #'icon' # current icons don't work; need to find new ones ---------- ADD LATER

    weather = {  # weather dictinoary
        "temperature": temperature,
        "description": description,
        "city": city_2,
    }

    context = {"weather": weather}

    return render(
        request, "home.html", context
    )  # home.html currently has "city temperatures"; is currently static and not using API
