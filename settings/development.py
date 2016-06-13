from .base import *


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'PORT': '5432',
        'NAME': 'bliss',
        'USER': 'cwb',
        'PASSWORD': 'password',
        'OPTIONS': {
            # "autocommit": True,
        },
    }
}

INSTALLED_APPS += [
    'debug_toolbar',
]

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'logging@rawdatatech.com'
EMAIL_HOST_PASSWORD = 'Abcd123#$'
EMAIL_PORT = 587
EMAIL_USE_TLS = True