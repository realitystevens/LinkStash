import os
from decouple import config
from django.core.wsgi import get_wsgi_application


if config('ENV') == 'PROD':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'linkstash.settings.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'linkstash.settings.development')

application = get_wsgi_application()
