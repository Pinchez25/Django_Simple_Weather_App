from django.shortcuts import render
import requests
from django.conf import settings
from django.http import HttpResponse


def index(request):
    data = {}
    if request.method == "POST":
        city = request.POST.get('city', '')

        request_ = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.API_KEY}")

        if request_.status_code == 200:
            response = request_.json()
            data = {
                "country": str(response['sys']['country']),
                "city": str(response['name']),
                "coordinates": str(f" Lon: {response['coord']['lon']} Lat: {response['coord']['lat']}"),
                "temperature": str(response['main']['temp'] - 273.15),
                "pressure": str(response['main']['pressure']),
                "humidity": str(response['main']['humidity']),
                "weather": str(response['weather'][0]['main']),
                "weather_description": str(response['weather'][0]['description']),
                'weather_icon': str(response['weather'][0]['icon'])

            }
        else:
            return HttpResponse("Error: An error occured! Check that you searched the correct city.")
        # http://openweathermap.org/img/w/10d.png

    return render(request, 'weather/index.html', data)
