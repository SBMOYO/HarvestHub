from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(r"ws/notify/(?P<room_name>\w+)/$", consumers.DailyUpdatesConsumer.as_asgi(), name="daily_updates"),
]