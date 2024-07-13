from . import views
from django.urls import path
from . import routing

urlpatterns = [
    path('', views.index, name='index'),
    path("<str:room_name>/", views.room, name="room"),
    path("twilio_webhook/", views.handle_incoming_whatsapp, name="twilio_webhook"),
]