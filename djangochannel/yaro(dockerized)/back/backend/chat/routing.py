# chat/routing.py
from django.urls import re_path,path

from . import consumers

wps = [
    # re_path(r'ws/chat/(?P<roomname>\w+)/$', consumers.ChatConsumer.as_asgi()),
    path('ws/chat/<str:roomname>/',consumers.ChatConsumer.as_asgi())
]