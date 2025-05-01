"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os
from decouple import config # Import decouple
from django.core.asgi import get_asgi_application

# Use decouple to get the settings module, default to development
settings_module = config('DJANGO_SETTINGS_MODULE', default='config.settings.development')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

application = get_asgi_application()
