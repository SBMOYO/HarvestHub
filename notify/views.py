from django.http import JsonResponse, HttpResponse
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
from .models import WhatsAppUser
from django.conf import settings

client = Client(settings.ACCOUNT_SID, settings.AUTH_TOKEN)


@csrf_exempt
def handle_incoming_whatsapp(request):
    if request.method == "POST":
        from_number = request.POST.get('From')
        profile_name = request.POST.get('ProfileName')
        body = request.POST.get('Body')

        if profile_name and from_number:
            # Check if the phone number already exists
            user, created = WhatsAppUser.objects.get_or_create(
                phone_number=from_number,
                defaults={'profile_name': profile_name}
            )

            if created:
                print(f"New user created: {user}")
            else:
                print(f"User already exists: {user}")

        # Process the incoming message
        response = MessagingResponse()
        response.message(f"Hello {profile_name}, you sent: '{body}' from  ({from_number})")

        return HttpResponse(str(response), content_type='text/xml')
