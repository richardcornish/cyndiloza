"""
Django settings for cyndiloza project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_ROOT = BASE_DIR
REPOSITORY_ROOT = os.path.join(PROJECT_ROOT, os.pardir)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ["CYNDILOZA_SECRET_KEY"]

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True


# Application definition

INSTALLED_APPS = (

    # Django apps, by default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Django apps, for this project
    'django.contrib.admindocs',
    'django.contrib.flatpages',
    'django.contrib.humanize',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'django.contrib.syndication',

    # Personal apps
    'cyndiloza.apps.about',
    'cyndiloza.apps.news',
    'cyndiloza.apps.people',
    'cyndiloza.apps.places',
    'cyndiloza.templatetags',

    # Third-party apps
    'robots',
    'sorl.thumbnail',
    'south',
    'typogrify',

)

MIDDLEWARE_CLASSES = (

    # First for caching
    'django.middleware.cache.UpdateCacheMiddleware',

    # Default middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    # Remove "www"
    'cyndiloza.middleware.remove_www.UrlMiddleware',

    # Flatpage fallback
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',

    # Last for caching
    'django.middleware.cache.FetchFromCacheMiddleware',

)

ROOT_URLCONF = 'cyndiloza.urls'

WSGI_APPLICATION = 'cyndiloza.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ['CYNDILOZA_DB_NAME'],
        'USER': os.environ['CYNDILOZA_DB_USER'],
        'PASSWORD': os.environ['CYNDILOZA_DB_PASS'],
        'HOST': '',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


# Templates
# https://docs.djangoproject.com/en/1.6/topics/templates/

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.load_template_source',
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

TEMPLATE_CONTEXT_PROCESSORS += (
    'cyndiloza.context_processors.site',
    'cyndiloza.context_processors.superuser',
    'cyndiloza.context_processors.map',
    'cyndiloza.context_processors.analytics',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)


# Project-specific settings

SITE_ID = 1

REMOVE_WWW = True

GOOGLE_MAPS_KEY = os.environ['CYNDILOZA_GOOGLE_MAPS']
