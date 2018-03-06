"""
WSGI config for china project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "website.settings")

from django.core.wsgi import get_wsgi_application  # noqa: E402
from whitenoise.django import DjangoWhiteNoise     # noqa: E402

application = DjangoWhiteNoise(get_wsgi_application())
