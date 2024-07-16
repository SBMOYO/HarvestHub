from celery import shared_task
from twilio.rest import Client
from .models import WhatsAppUser
from django.conf import settings

client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)


@shared_task
def send_daily_whatsapp_updates():

    users = WhatsAppUser.objects.all()
    for user in users:
        message = client.messages.create(
            body=f'Hello {user.profile_name} Here is your daily update! great to see you again',
            from_='whatsapp:+14155238886',
            to=user.phone_number
        )
        print(f"Sent message to {user.profile_name} ({user.phone_number})")
