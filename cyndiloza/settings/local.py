"""
Local development settings
"""

from cyndiloza.settings.base import *


DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1'
]

MEDIA_ROOT = os.path.join(REPOSITORY_ROOT, 'assets', 'media')

MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(REPOSITORY_ROOT, 'assets', 'static')

STATIC_URL = '/static/'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

THUMBNAIL_DUMMY = True

THUMBNAIL_DUMMY_SOURCE = 'http://placehold.it/%(width)sx%(height)s'
