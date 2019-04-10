"""
WSGI config for web_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = BASE_DIR+'/web_blog'
os.environ['DJANGO_SETTINGS_MODULE'] = 'path.settings'

application = get_wsgi_application()
