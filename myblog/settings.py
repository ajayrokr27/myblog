"""
Django settings for myblog project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'sxk2lj03gbianyqy+%&a$0^hdu_9+63wplj@h^2kz5awsqb4at'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    # 'django_wysiwyg',
    #'registration',
     # The default Address and country models

)
ACCOUNT_ACTIVATION_DAYS=7
EMAIL_HOST='localhost'
EMAIL_PORT=8000
EMAIL_HOST_USER='root'
EMAIL_HOST_PASSWORD=''

DJANGO_WYSIWYG_FLAVOR = "ckeditor"

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'myblog.urls'

WSGI_APPLICATION = 'myblog.wsgi.application'
TEMPLATE_CONTEXT_PROESSORS = (
'django.core.context_processors.request',
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'
        'ENGINE': 'django.db.backends.mysql',
        # Or the path to the database file if using sqlite3
        'NAME': 'myblog',
        # The following settings are not used with sqlite3
        'USER': 'ajay',
        'PASSWORD': '12345',
        # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP
        'HOST': '',
        # Set to empty string for default
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
APP_NICE_SHORT_NAME = "MySite" # a short name for your site
SERVER_EMAIL = "MySite <noreply@example.org>" # From: address on verification emails
REGISTRATION_ASK_USERNAME = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
