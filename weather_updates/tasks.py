from celery import shared_task
from twilio.rest import Client
from notify.models import WhatsAppUser
from django.conf import settings
import os

client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)

@shared_task
def daily_weather_updates_task(message_body):

    users = WhatsAppUser.objects.all()
    for user in users:
        client.messages.create(
            body=message_body,
            from_='whatsapp:+14155238886',
            to=user.phone_number
        )
        print(f"Sent message to {user.profile_name} ({user.phone_number})")
