"""
ASGI config for webApp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

### UTILISATION SANS CHANNELS
import os
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webApp.settings')
application = get_asgi_application()

##UTILISATION AVEC CHANNELS
#import os
#from django.core.asgi import get_asgi_application
#
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webApp.settings')
#
#from channels.auth import AuthMiddlewareStack
#from channels.routing import ProtocolTypeRouter , URLRouter
#from main import routing
#
#application = ProtocolTypeRouter(
#	{
#		"http" : get_asgi_application() ,
#		"websocket" : AuthMiddlewareStack(
#			URLRouter(
#				routing.websocket_urlpatterns
#			)
#		)
#	}
#)


