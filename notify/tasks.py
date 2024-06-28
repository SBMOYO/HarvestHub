from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

@shared_task
def send_daily_updates():
    message_content = "Your daily update: Check out our new products!"
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)('daily_updates', {'type': 'send_daily_message', 'message': message_content})