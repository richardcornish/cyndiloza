"""
Production settings
"""

from cyndiloza.settings.base import *


DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = [
    '.cyndiloza'
]

MEDIA_ROOT = '/home/richardcornish/webapps/cyndiloza_assets/media/'

MEDIA_URL = 'http://assets.cyndiloza.com/media/'

STATIC_ROOT = '/home/richardcornish/webapps/cyndiloza_assets/static/'

STATIC_URL = 'http://assets.cyndiloza.com/static/'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': 'unix:/home/richardcornish/cache/memcached.sock',
    }
}

CACHE_MIDDLEWARE_ALIAS = 'default'
CACHE_MIDDLEWARE_SECONDS = 600
CACHE_MIDDLEWARE_KEY_PREFIX = '2'
