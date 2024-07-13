from django.http import JsonResponse, HttpResponse
from twilio.twiml.messaging_response import MessagingResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import json

def index(request):
    return render(request, "notify/index.html")

def room(request, room_name):
    return render(request, "notify/room.html", {"room_name": room_name})

@csrf_exempt
def handle_incoming_whatsapp(request):
    if request.method == "POST":
        incoming_msg = request.POST.get("Body", "").lower()
        room_name = request.POST.get("From", "")  # Use the sender's number as the room name

        # Process the incoming message (e.g., extract relevant info)
        # Implement your logic here to generate a response

        # Example: Echo the received message back
        response = MessagingResponse()
        response.message(f"You said: {incoming_msg}")

        # Send message to WebSocket consumer
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            f"daily_updates_{room_name}",
            {"type": "notify.message", "message": response.to_xml()}
        )

        return HttpResponse(str(response), content_type='text/xml')
    return JsonResponse({"error": "Invalid request method."})
