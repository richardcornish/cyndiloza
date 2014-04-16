"""
Local development settings
"""

from cyndiloza.settings.base import *


DEBUG = True

TEMPLATE_DEBUG = True

MEDIA_ROOT = os.path.join(REPOSITORY_ROOT, 'assets', 'media')

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(REPOSITORY_ROOT, 'assets', 'static')

STATIC_URL = '/static/'
