from .base import *


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'PORT': '5432',
        'NAME': 'bledb',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'OPTIONS': {
            # "autocommit": True,
        },
    }
}

INSTALLED_APPS += [
    'debug_toolbar',
]
