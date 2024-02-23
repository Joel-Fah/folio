import dj_database_url
from .base import *

# Settings overrides for development environment

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1%%^y@_&a-^p%#c*zuhy(b@%b79gdj!nabf0jsidcd^)(hgph@'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '*']

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
    
    'render': dj_database_url.parse("postgres://folio_pw83_user:XBathhJkVCCUbQkBK5ZywjzJZg8rJYaK@dpg-cnahoetjm4es73c89ri0-a.oregon-postgres.render.com/folio_pw83"),
    'supabase': dj_database_url.parse("postgres://postgres.yzstcegfjzycpunmiphd:Q01l1XZv1RMHqqZE@aws-0-eu-central-1.pooler.supabase.com:5432/postgres"),
}

# Add compression and caching support for whitenoise

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}