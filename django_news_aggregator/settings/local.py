# SECURITY WARNING: don't run with debug turned on in production!
from django_news_aggregator.settings.base import *


DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']

INSTALLED_APPS += [

]

MIDDLEWARE += [
    
]

# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
        'TIMEOUT': 1296000,
    }
}

# CELERY SETTINGS
CELERY_BROKER_URL = 'redis://:p31597f53c1a12263faad1db77cd4d0b6a20b35c04d66121d01d7b11efc4a944c@ec2-3-213-255-205.compute-1.amazonaws.com:16570'
CELERY_RESULT_BACKEND = 'redis://:p31597f53c1a12263faad1db77cd4d0b6a20b35c04d66121d01d7b11efc4a944c@ec2-3-213-255-205.compute-1.amazonaws.com:16570'
# CELERY_BROKER_URL = 'redis://localhost:6379'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'

CELERY_IMPORTS = (
    'posts.tasks'
)