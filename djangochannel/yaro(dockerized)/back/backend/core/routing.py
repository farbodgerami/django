from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,URLRouter
import chat.routing
from django.core.asgi import get_asgi_application

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application=ProtocolTypeRouter({
       "http": get_asgi_application(),
    'websocket':AuthMiddlewareStack(
        URLRouter(
            chat.routing.wps,  
        )
    )
})