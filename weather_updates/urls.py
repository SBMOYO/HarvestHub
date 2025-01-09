from django.urls import path
from . import views


urlpatterns = [
    path("twilio_webhook_updates/", views.daily_weather_updates, name="twilio_webhook_updates"),
]