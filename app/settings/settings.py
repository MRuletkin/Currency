import os
from pathlib import Path

from celery.schedules import crontab

from django.urls import reverse_lazy

import environ

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR.parent, '.env'))

env = environ.Env(
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, []),

    RABBITMQ_DEFAULT_USER=(str, 'guest'),
    RABBITMQ_DEFAULT_PASS=(str, 'guest'),
    RABBITMQ_DEFAULT_PORT=(str, '5672'),
    RABBITMQ_DEFAULT_HOST=(str, 'localhost'),

    POSTGRES_HOST=(str, 'localhost'),
    POSTGRES_PORT=(str, '5432'),

    MEMCACHED_HOST=(str, 'localhost'),
    MEMCACHED_PORT=(str, '11211'),
)

DEBUG = env('DEBUG')

ALLOWED_HOSTS = env('ALLOWED_HOSTS')

SECRET_KEY = env('SECRET_KEY')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'phonenumber_field',

    'silk',
    'django_extensions',
    'debug_toolbar',
    'rangefilter',
    'import_export',
    'crispy_forms',
    'django_tables2',
    'rest_framework',

    'currency',
    'accounts',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'silk.middleware.SilkyMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'currency.middlewares.RequestResponseTimeMiddleware',
]

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [
            BASE_DIR / 'templates',
        ],

        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env('POSTGRES_DB'),
        'USER': env('POSTGRES_USER'),
        'PASSWORD': env('POSTGRES_PASSWORD'),
        'HOST': env('POSTGRES_HOST'),
        'PORT': env('POSTGRES_PORT'),
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
        'LOCATION': f'{env("MEMCACHED_HOST")}:{env("MEMCACHED_PORT")}',
    }
}

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = 'currency-django-bucket'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }
# AWS_LOCATION = 'static'
#
# STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]
STATIC_ROOT = '/tmp/static'

# DEFAULT_FILE_STORAGE = 'app.settings.storage_backends.MediaStorage'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.parent / 'static_content' / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587  # smtp, http: 80, https: 443
# EMAIL_HOST_USER = 'testtestapp454545@gmail.com'
# EMAIL_HOST_PASSWORD = 'qwerty123456qwerty'
DEFAULT_FROM_EMAIL = 'testtestapp454545@gmail.com'

LOGIN_REDIRECT_URL = reverse_lazy('index')
LOGOUT_REDIRECT_URL = reverse_lazy('index')
LOGIN_URL = reverse_lazy('login')
AUTH_USER_MODEL = 'accounts.user'

INTERNAL_IPS = [
    '127.0.0.1',
]

DOMAIN = 'localhost:8000'
HTTP_SCHEMA = 'http'

REST_FRAMEWORK = {
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

# CELERY_BROKER_URL = 'amqp://guest:guest@localhost:5672//'

CELERY_BROKER_URL = f'amqp://{env("RABBITMQ_DEFAULT_USER")}:' \
                    f'{env("RABBITMQ_DEFAULT_PASS")}@' \
                    f'{env("RABBITMQ_DEFAULT_HOST")}:{env("RABBITMQ_DEFAULT_PORT")}//'


CELERY_BEAT_SCHEDULE = {
    'parse_privatbank': {
        'task': 'currency.tasks.parse_privatbank',
        'schedule': crontab(minute='*/1')
    },
    'parse_monobank': {
        'task': 'currency.tasks.parse_monobank',
        'schedule': crontab(minute='*/5')
    },
    'parse_vkurse': {
        'task': 'currency.tasks.parse_vkurse',
        'schedule': crontab(minute='*/1')
    },
    'parse_alfabank': {
        'task': 'currency.tasks.parse_alfabank',
        'schedule': crontab(minute='*/1')
    },
    'parse_oschadbank': {
        'task': 'currency.tasks.parse_oschadbank',
        'schedule': crontab(minute='*/1')
    },
    'parse_parse_obmen_dp_ua': {
        'task': 'currency.tasks.parse_obmen_dp_ua',
        'schedule': crontab(minute='*/1')
    },
}

CRISPY_TEMPLATE_PACK = 'bootstrap4'

PHONENUMBER_DB_FORMAT = "INTERNATIONAL"
