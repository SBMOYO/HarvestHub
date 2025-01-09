from . import views
from django.urls import path

urlpatterns = [
    path("twilio_webhook/", views.handle_incoming_whatsapp, name="twilio_webhook"),
]