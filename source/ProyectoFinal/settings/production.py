from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['santiagonrod.pythonanywhere.com']

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd55ffjodq2g19l',
        'USER': 'hdplfawgkaeyvc',
        'PASSWORD': '294b65ea69093b7f2d56b78749cca809a91aa3a4f65deb73037b802b479103a9',
        'HOST': 'ec2-34-235-31-124.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
