"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get('DEBUG', 0)))

ALLOWED_HOSTS = []
ALLOWED_HOSTS.extend(
    filter(
        None,
        os.environ.get('ALLOWED_HOSTS', '').split(','),
    )
)



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social_django',
    'phones',
    'rest_framework',
    'knox',
    'corsheaders',
    'django_filters',
    'crispy_forms'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    'corsheaders.middleware.CorsPostCsrfMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR/'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends'
            ],
        },
    },
]

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.environ.get('DB_HOST'),
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASS'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_USE_SSL = False
#EMAIL_FROM = 'podolskiydmitry@gmail.com'
#EMAIL_HOST_USER = 'podolskiydmitry@gmail.com'
#EMAIL_HOST_PASSWORD = 'sjijfcbejtnhcihv'
EMAIL_FROM = 'garasfamal@gmail.com'
EMAIL_HOST_USER = 'garasfamal@gmail.com'
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')#'dxylgvwvzrqjrwmd'#'bjlxnmfeqhmurdxu'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

#STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')
STATIC_URL = '/static/static/'
MEDIA_URL = '/static/media/'

MEDIA_ROOT = '/vol/web/media'
STATIC_ROOT = '/vol/web/static'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES':[
    'rest_framework.renderers.JSONRenderer',
    'rest_framework.renderers.BrowsableAPIRenderer'#отвечает за отображение сайта
],
'DEFAULT_PERMISSION_CLASSES':[
    #'rest_framework.permissions.IsAuthenticated',
#базовое ограничение для всех апи классов если конечно они не имеют свои ограничения permission_classes
],
'DEFAULT_AUTHENTICATION_CLASSES': [
    'knox.auth.TokenAuthentication',
    'rest_framework.authentication.TokenAuthentication',
    #'rest_framework.authentication.BasicAuthentication',
    'rest_framework.authentication.SessionAuthentication',
                                   ],
'DEFAULT_FILTER_BACKENDS': [
    'django_filters.rest_framework.DjangoFilterBackend'
],
'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
'PAGE_SIZE': 5
}

CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = []
CORS_ALLOWED_ORIGINS.extend(filter(None,os.environ.get('ALLOWED_HOSTS_HTTP', '').split(','),))# If this is used, then not need to use `CORS_ALLOW_ALL_ORIGINS = True`
CORS_ALLOWED_ORIGIN_REGEXES = []
CORS_ALLOWED_ORIGIN_REGEXES.extend(filter(None,os.environ.get('ALLOWED_HOSTS_HTTP', '').split(','),))
CORS_ORIGIN_WHITELIST = "http://139.59.15.161:3000"
CORS_ORIGIN_ALLOW_ALL = False#True

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
]
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home'

LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'login'

SOCIAL_AUTH_GITHUB_KEY = '81cfb1c6ffebeecbc567'
SOCIAL_AUTH_GITHUB_SECRET = 'f02bddf1c3b58b84ef6137cb03c26517f354f155'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1048832586384-t6jth6pg590556idi71mpk338d1em9fa.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

STRIPE_PUBLIC_KEY='pk_test_51MfqxGEFAX4ybJinRwTbicBTgxT1UqviPkJcJBAluxdhRJeHMRBhlyBPvxe8OvxnCsPXkX6LxI4RS4bO0zaZtIzk00345MLw6Q'
STRIPE_SECRET_KEY='sk_test_51MfqxGEFAX4ybJinIBCSCTszLqbp8ioWGdKE6uqjB9R5baPyG7wxHHY8iAvLbHDLkHgjuDq5wcoIvl7yBOT8uYT100Wwpc6Dbx'
STRIPE_WEBHOOK_SECRET='whsec_32bb58713348b20f8c87c258e467c2af33348bc1c54b06ec36708e0a83a8b22c'
