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
    'default': dj_database_url.parse(os.getenv("DATABASE_URL"))
}

# AWS S3 media storage management
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_S3_SIGNATURE_NAME = os.getenv("AWS_S3_SIGNATURE_NAME"),
AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME")
AWS_S3_ADDRESSING_STYLE = "virtual"
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL =  None
AWS_S3_VERITY = True
DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"