import dj_database_url
from .base import *

# Settings overrides for development environment

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1%%^y@_&a-^p%#c*zuhy(b@%b79gdj!nabf0jsidcd^)(hgph@'

DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '192.168.8.109']

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'dev_sqlite': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "folio", 
        'USER': "postgres",
        'PASSWORD': "Ec@n@mics1@",
        'HOST': "localhost", 
        'PORT': 5432,
    },
    
    'production': dj_database_url.parse("postgres://folio_gyf8_user:uEDyQZlhJklHPH5rMFhTciwEn2fMaNDi@dpg-cm9jmqun7f5s73cmtal0-a/folio_gyf8"),
}