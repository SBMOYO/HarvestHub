from dotenv import load_dotenv
import os
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from django.conf import settings
from django.shortcuts import render, HttpResponse
import requests
from notify.models import WhatsAppUser
from .tasks import daily_weather_updates_task

load_dotenv()
client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)


def daily_weather_updates(request):

    place = "Zimbabwe"
    api_key = os.getenv('WEATHERAPI_API_KEY')
    
    api_url = f"https://api.weatherapi.com/v1/forecast.json"
    params = {
        'key': api_key,
        'q': place,
        'days': 3
    }
    headers = {
        'accept': 'application/json'
    }

    response = requests.get(api_url, params=params, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        message_body = f"
            Weather updates for {place} for the following days are as follows: 
            Temperature: {data['forecast']['forecastday'][0]['day']['avgtemp_c']}°C
            Humidity: {data['forecast']['forecastday'][0]['day']['avghumidity']}%
            Wind Speed: {data['forecast']['forecastday'][0]['day']['maxwind_kph']} km/h
            Rain: {data['forecast']['forecastday'][0]['day']['totalprecip_mm']} mm
            Cloud Cover: {data['forecast']['forecastday'][0]['day']['avghumidity']}%
            UV Index: {data['forecast']['forecastday'][0]['day']['uv']}
        "
        daily_weather_updates_task.delay(message_body)
    else:
        return HttpResponse("Error: Unable to retrieve data from the API.", status=response.status_code)
