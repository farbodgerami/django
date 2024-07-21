"""
ASGI config for asyncsync project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'asyncsync.settings')

# application = get_asgi_application()


import os
import django
 
from django.core.asgi import get_asgi_application
from django.core.wsgi import get_wsgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "asyncsync.settings")
django.setup()


from channels.auth import AuthMiddlewareStack

application = ProtocolTypeRouter({
    "http": get_asgi_application(), 
})
