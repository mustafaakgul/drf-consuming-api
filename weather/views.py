from django.shortcuts import render
import requests
from .models import *
import json
from types import SimpleNamespace

def weather(request):
    response = requests.get('https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'.format(lat=40.9910, lon=28.6498, API_KEY='21f05ca1a3538ed5f99b1df5aa1078a0'))
    #json = response.json()

    """
    {'coord': {'lon': 28.6498, 'lat': 40.991}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'base': 'stations', 'main': {'temp': 298.62, 'feels_like': 298.71, 'temp_min': 294.1, 'temp_max': 298.62, 'pressure': 1013, 'humidity': 57}, 'visibility': 10000, 'wind': {'speed': 3.09, 'deg': 280}, 'clouds': {'all': 75}, 'dt': 1654507077, 'sys': {'type': 1, 'id': 6970, 'country': 'TR', 'sunrise': 1654482843, 'sunset': 1654536859}, 'timezone': 10800, 'id': 6947640, 'name': 'Beylikdüzü', 'cod': 200}
    """

    #x = json.loads(json, object_hook=lambda d: SimpleNamespace(**d))
    #print(x)
    #Basetable.objects.create(**json)

    j = json.loads(response.text)
    tab = Basetable(**j)
    print(tab)

    context = {

    }
    return render(request, 'weather/weather.html', context)