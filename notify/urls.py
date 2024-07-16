from . import views
from django.urls import path
from . import celery

urlpatterns = [
    path("twilio_webhook/", views.handle_incoming_whatsapp, name="twilio_webhook"),
]