import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter
from django.urls import re_path
from chat import consumers

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'telegrambot.settings')

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
        ]
        )
    ),
    'http': get_asgi_application(),
})
