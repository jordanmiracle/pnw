"""
Django settings for PNWproject project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import json
import dj_database_url
from decouple import config
import boto3
import dj_database_url
import django_heroku
from storages.backends.s3boto3 import S3Boto3Storage
from django.core.exceptions import ImproperlyConfigured


# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c@v-7n2$0n!eh_-!)3yb8zpj_lm4*lu+n2$@^2(@zs%(#tpwrr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SITE_ID = 1

ALLOWED_HOSTS = ['127.0.0.1', "localhost", "pnwtree.herokuapp.com", "pnwtreescapes.com", "*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website.apps.WebsiteConfig',
    'photos.apps.PhotosConfig',
    'pwa',
    'storages',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'PNWproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'PNWproject.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
# }


with open(os.path.join(BASE_DIR, 'secrets.json')) as secrets_file:
    secrets = json.load(secrets_file)


def get_secret(setting, secrets=secrets):
    """Get secret setting or fail with ImproperlyConfigured"""
    try:
        return secrets[setting]
    except KeyError:
        raise ImproperlyConfigured("Set the {} setting".format(setting))


if DEBUG:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'USER': 'jordanmiracle',
            'NAME': 'pnwdb',
            'HOST': 'localhost',
            'PASSWORD': get_secret('DB_PASSWORD'),
            'PORT': '5432',
        },
    }

FIXTURE_DIRS = [
    os.path.join(BASE_DIR, "fixtures")
]

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# COMPRESS_URL = "https://pnwtree.s3.amazonaws.com/"
# STATIC_URL = "https://%s%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
# STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, 'static')
# ]
# STATIC_ROOT = BASE_DIR / 'staticfiles'
# COMPRESS_ROOT = BASE_DIR / 'staticfiles'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')serving media files in django
## STATICFILES_DIRS = [
##    BASE_DIR / "static",
##
## ]
# STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, 'static')
# ]
#MEDIA_ROOT = BASE_DIR / 'media/images'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'images')
#MEDIA_URL = '/images/'
# MEDIA_URL = '/images/'
#
# STATICFILES = [
#    BASE_DIR / 'static'
# ]
# STATIC_ROOT = ''


# S3 bucket config
# if not DEBUG:
# AWS_ACCESS_KEY_ID = 'AKIAXCHWTHMX4UYTYOOI'
# AWS_SECRET_ACCESS_KEY = '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'
# AWS_STORAGE_BUCKET_NAME = 'pnwtree'
# AWS_S3_FILE_OVERWRITE = False
# AWS_DEFAULT_ACL = None
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# MEDIAFILES_LOCATION = 'media'
# AWS_QUERYSTRING_AUTH = False

# COMPRESS_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# STATICFILES_STORAGE = 'storaN6NuYCG0NDVts/ICk0LSAg/1hQPSJO1uoGnk9b6Jges.backends.s3boto3.S3StaticStorage'
AWS_ACCESS_KEY_ID = get_secret('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_secret('AWS_ACCESS_KEY_ID')
AWS_STORAGE_BUCKET_NAME = 'pnwtree'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# AWS_S3_OBJECT_PARAMETERS = {
#    'CacheControl': 'max-age=86400',
# }
AWS_LOCATION = 'static'
DEFAULT_FILE_STORAGE = 'PNWproject.storage_backends.MediaStorage'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, 'static'),
# ]
PUBLIC_MEDIA_LOCATION = 'media'
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / 'media'
# ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
# STATICFILES_FINDERS = (
#    'django.contrib.staticfiles.finders.FileSystemFinder', 'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# )

PWA_APP_NAME = 'PNW Tree & Landscaping'
PWA_APP_DESCRIPTION = "Family owned tree and landscaping service that serves Whatcom, Skagit, and Island counties. " \
                      "Safety, speed, and efficiency set us apart. We offer 24/7 emergency services, along with a " \
                      "wide array of other tree and land services. "
PWA_APP_THEME_COLOR = '#2a4027'
PWA_APP_BACKGROUND_COLOR = '#CED2D9'
PWA_APP_DISPLAY = 'standalone'
PWA_APP_SCOPE = '/'
PWA_APP_ORIENTATION = 'any'
PWA_APP_START_URL = '/'
PWA_APP_STATUS_BAR_COLOR = 'default'
PWA_APP_ICONS = [
    {
        'src': 'static/website/images/pnwtree-and-landscaping-logo.png',
        'sizes': '160x160'
    }
]
PWA_APP_ICONS_APPLE = [
    {
        'src': 'static/website/images/pnwtree-and-landscaping-logo.png',
        'sizes': '160x160'
    }
]
PWA_APP_SPLASH_SCREEN = [
    {
        'src': 'static/website/images/pnwtree-and-landscaping-logo.png',
        'media': '(device-width: 320px) and (device-height: 568px) and (-webkit-device-pixel-ratio: 2)'
    }
]
PWA_APP_DIR = 'ltr'
PWA_APP_LANG = 'en-US'

## Heroku
# heroku database settings
if not DEBUG:
    django_heroku.settings(locals(), staticfiles=False)
    DATABASES = {'default': dj_database_url.config(conn_max_age=600, ssl_require=True)}
