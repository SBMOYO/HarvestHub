import json

from channels.generic.websocket import AsyncWebsocketConsumer
from twilio.twiml.messaging_response import MessagingResponse

class DailyUpdatesConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"daily_updates_{self.room_name}"

        # Join room group
        await self.channel_layer.group_add(self.room_group_name, self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(self.room_group_name, self.channel_name)

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        incoming_msg = text_data_json.get("message", "").lower()
        # Process the incoming message (e.g., extract relevant info)
        # Implement your logic here to generate a response

        # Example: Echo the received message back
        response = MessagingResponse()
        response.message(f"You said: {incoming_msg}")

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name, {"type": "notify.message", "message": response.to_xml()}
        )

    # Receive message from room group
    async def notify_message(self, event):
        message_content = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message_content}))