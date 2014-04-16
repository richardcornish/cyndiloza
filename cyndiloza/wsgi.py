import os

os.environ["DJANGO_SETTINGS_MODULE"] = os.environ["CYNDILOZA_DSM"]

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
