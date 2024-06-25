from .base import *
import dj_database_url

# Your development specific settings here

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = os.getenv("DEBUG", False) == 'True'

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(" ")

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.parse(os.getenv("DATABASE_URL_SUPABASE"))
}

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
SUPABASE_BUCKET_NAME = os.getenv("SUPABASE_BUCKET_NAME")

DEFAULT_FILE_STORAGE = 'core.supabase_storage.SupabaseStorage'

# Supabase media storage management
# DEFAULT_FILE_STORAGE = 'django_storage_supabase.supabase'
# SUPABASE_API_KEY = os.getenv("SUPABASE_API_KEY")
# SUPABASE_URL = os.getenv("SUPABASE_URL")
# SUPABASE_ROOT_PATH = '/dir/'