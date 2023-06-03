"""
Celery tasks for places app
"""
import os

import requests
from django.utils import timezone

from DDCTT.celery import app
from .models import Place, WeatherInPlace


@app.task
def get_places_weather():
    """
    Update or create WeatherInPlace models with new data from OpenWeatherApi
    """
    places = Place.objects.all()
    for place in places:
        _, lat, lon = str(place.point).split()
        lat = lat[1:]
        lon = lon[:-1]
        key = os.environ.get('OPEN_WEATHER_API_KEY')
        url = os.environ.get('OPEN_WEATHER_API_URL')
        params = {'APPID': key, 'lat': lat, 'lon': lon, 'units': 'metric'}
        result = requests.get(url, params=params)
        weather = result.json()
        temp = weather['main']['temp']
        humidity = weather['main']['humidity']
        pressure = weather['main']['pressure']
        wind_deg = weather['wind']['deg']
        wind_speed = weather['wind']['speed']
        WeatherInPlace.objects.update_or_create(
            place=place,
            defaults={
                'temp': temp,
                'humidity': humidity,
                'pressure': pressure,
                'wind_deg': wind_deg,
                'wind_speed': wind_speed,
                'date_of_reading': timezone.now()
            }
        )
