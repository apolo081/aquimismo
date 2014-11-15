import sys
import os
from .settings import BASE_DIR
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'aquimismo',
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': 'minrock',
        'PASSWORD': 'bxrrapido'
    }
}
