from pathlib import Path
import os
from os.path import join
from django.conf.global_settings import AUTH_USER_MODEL
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-z7caul6@*+v4qn1r+c7)ty*3d#0qis=b&m#ftu1fq$q9-5)11h'

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'rest_framework',
    'drf_spectacular',
    'apps',
    "django.contrib.staticfiles",
    "graphene_django",

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "django.middleware.locale.LocaleMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'root.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'root.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        "NAME": "postgres",
        "USER": "postgres",
        "PASSWORD": "1",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

REST_FRAMEWORK = {

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Your Project API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,

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

PARLER_LANGUAGES = {
    None: (
        {'code': 'en', },
        {'code': 'uz', },
    ),
    'default': {
        'fallbacks': ['en'],
        'hide_untranslated': False,
    }
}
PARLER_DEFAULT_LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGES = [
    ('en', _('English')),
    ('uz', _('Uzbek')),
]

LANGUAGE_CODE = 'en'

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

GRAPHENE = {
    "SCHEMA": "root.schema.schema"
}
