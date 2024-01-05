"""
WSGI config for btre project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/

specification that defines how a web server communicates with the web application and how web apps can be chained together to 
process one request, basically deals with hosting your site so that people can access it
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "btre.settings")

application = get_wsgi_application()
