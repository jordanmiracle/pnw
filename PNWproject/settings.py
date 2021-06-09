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
import psycopg2


# Build paths inside the project like this: BASE_DIR / 'subdir'.
from django.conf.global_settings import DATABASES

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'sdfjnliusrnf$^&*nsaloiser%%&*fk330fkgk6;l4382')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1', "localhost", "floating-hamlet-66379.herokuapp.com", "www.pnwtreescapes.com", "pnwtreescapes.com"]

# Deploy checklist#
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 1
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

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
    'compressor',
    'pwa',
    'storages',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
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
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'USER': 'emjdftgkxgunmc',
#        'NAME': 'd7lvq30bmeq5ve',
#        'HOST': 'ec2-54-243-92-68.compute-1.amazonaws.com',
#        'PASSWORD': '714333c0ecac8d62e83f757d006ddf2b860810d10296bc3aab9c332abfbda7bb',
#        'PORT': 5432,
#
#
#
#    }
#}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}

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

#STATICFILES_DIRS = [
#   os.path.join(BASE_DIR, 'static')
#]

MEDIA_ROOT = BASE_DIR / 'static/images'
MEDIA_URL = '/images/'

#STATICFILES = [
#    BASE_DIR / 'static'
#]

STATIC_ROOT = BASE_DIR / 'staticfiles'
#STATIC_TMP = BASE_DIR / 'static'

#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


## AWS S3 ##


AWS_ACCESS_KEY_ID = 'AKIAXCHWTHMXUSTYOJPM'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'django-personal-s3'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_LOCATION = 'static'
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

AWS_S3_FILE_OVERWRITE = True
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#AWS_LOCATION = 'static'

AWS_DEFAULT_ACL = 'public-read'




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

##Heroku##
# Heroku: Update database configuration from $DATABASE_URL.
# import dj_database_url
# import django_heroku
#
# DATABASE_URL = os.environ['DATABASE_URL']
#
# conn = psycopg2.connect(DATABASE_URL, sslmode='require')
#
# DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
# django_heroku.settings(locals())


