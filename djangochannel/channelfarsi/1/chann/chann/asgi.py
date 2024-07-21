from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.sessions import SessionMiddlewareStack
from channels.security.websocket import OriginValidator, AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application
from echo import routing as echo_routing

django_asgi_app = get_asgi_application()
application = ProtocolTypeRouter({
    "http": django_asgi_app,
    'websocket': AllowedHostsOriginValidator(
        SessionMiddlewareStack(
            AuthMiddlewareStack(
                URLRouter(
                    echo_routing.websocket_urlpatterns
                )
            )
        )
    )
})
