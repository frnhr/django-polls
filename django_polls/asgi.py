"""
ASGI config for django_polls project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application  # type: ignore

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_polls.settings')

application = get_asgi_application()
