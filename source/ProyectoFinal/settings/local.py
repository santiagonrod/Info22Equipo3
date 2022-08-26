from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': 'Proyecto',
        #'USER': 'postgres',
        #'PASSWORD': 'grupo3info2022',
        #'HOST': '127.0.0.1',
        #'PORT': '5432',
    }
}

