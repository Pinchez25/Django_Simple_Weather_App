import requests as r
from django.conf import settings
from django.http import HttpResponse


def default_weather(request):
    """
       Shows the weather of the user based on their 
       public ip info
    """
    ipinfo = r.get('http://ipinfo.io/json').json()
    city = ipinfo['city']
    country = ipinfo['country']
    latitude = ipinfo['loc'].split(',')[0]
    longitude = ipinfo['loc'].split(',')[1]
    request_ = r.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={settings.API_KEY}")

    if request_.status_code == 200:
        response = request_.json()
        data = {
            'current_city': city,
            "c_country": str(country),
            "c_coordinates": str(f" Lon: {longitude} Lat: {latitude}"),
            "c_temperature": str(response['main']['temp'] - 273.15),
            "c_pressure": str(response['main']['pressure']),
            "c_humidity": str(response['main']['humidity']),
            "c_weather": str(response['weather'][0]['main']),
            "c_weather_description": str(response['weather'][0]['description']),
            'c_weather_icon': str(response['weather'][0]['icon'])

        }
    else:
        return HttpResponse("Error: An error occured! Check that you searched the correct city.")

    return data
