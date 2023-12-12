from decouple import config

DJANGO_DB_NAME = config('DJANGO_DB_NAME', cast=str)
DJANGO_DB_USER = config('DJANGO_DB_USER', cast=str)
DJANGO_DB_PASSWORD = config('DJANGO_DB_PASSWORD', cast=str)
DJANGO_DB_HOST = config('DJANGO_DB_HOST', cast=str)
DJANGO_DB_PORT = config('DJANGO_DB_PORT', cast=str)

if all([DJANGO_DB_NAME, DJANGO_DB_USER, DJANGO_DB_PASSWORD, DJANGO_DB_HOST, DJANGO_DB_PORT]):

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DJANGO_DB_NAME,
        'USER': DJANGO_DB_USER,
        'PASSWORD': DJANGO_DB_PASSWORD,
        'HOST': DJANGO_DB_HOST,
        'PORT': DJANGO_DB_PORT,
        'OPTIONS': {'sslmode': 'require'},
    }
    }