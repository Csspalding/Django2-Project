"""
WSGI config for Dynamo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os
# Error with django import initially, problem solved with config by reading up https://ruddra.com/posts/vs-code-for-python-development/ and adding pyLint django plugins code in settings.json

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Dynamo.settings')

application = get_wsgi_application()
