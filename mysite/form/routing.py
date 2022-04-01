# chat/routing.py
from django.urls import re_path

from . import consumers
from django.urls import path

websocket_urlpatterns = [
    path('ws/form/', consumers.ChatConsumer),

]

