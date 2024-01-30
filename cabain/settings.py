"""
Django settings for cabain project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import pymysql
pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Redirecciona a menu después de iniciar sesión (Redirecciona por defecto a /accounts/profile/)
LOGIN_REDIRECT_URL = '/menu_principal/'
LOGIN_URL = '/cuenta/login/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+1+o8as375p_ogyz4)_()cw+k%@13p3rgn43kvq@%!me63j)41'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

MESSAGE_STORAGE= "django.contrib.messages.storage.cookie.CookieStorage"



# Application definition

INSTALLED_APPS = [
    'cabin_APP',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',

    #paquetes del proyecto
    'crispy_forms',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cabin_APP.middleware.AutoDeactivateUsersMiddleware',
]


ROOT_URLCONF = 'cabain.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'cabain.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
            'NAME': 'cabinsproyect',
            'USER': 'root',
            'PASSWORD': '',
        'OPTIONS': {
            'sql_mode': 'STRICT_TRANS_TABLES',
        },
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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'es-esp'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS= [os.path.join(BASE_DIR, 'static')]

CRISPY_TEMPLATE_PACK = 'bootstrap4'
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Configuración de Transbank
BASE_URL = 'http://127.0.0.1:8000/'
WEBPAY_URL = 'https://webpay3gint.transbank.cl/rswebpaytransaction/api/webpay/v1.2/transactions'
WEBPAY_ID = '597055555532' # CODIGO COMERCIO
WEBPAY_SECRET = '579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C' #CLAVE SECRETA

# Configuración de correo electrónico para el envío de enlaces de restablecimiento de contraseña
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Cambia esto al servidor de correo que estés utilizando (por ejemplo, 'smtp.gmail.com' para Gmail).
EMAIL_PORT = 587  # Cambia esto al puerto del servidor de correo (587 para TLS en Gmail).
EMAIL_USE_TLS = True  # Utiliza TLS para cifrar la conexión (cambia a False si tu servidor de correo no lo admite).

# Configura las credenciales de tu cuenta de correo electrónico
EMAIL_HOST_USER = 'dominatuproyecto@gmail.com'  # Cambia esto a tu dirección de correo electrónico.
EMAIL_HOST_PASSWORD = 'jemu bioh kjex xtar'  # Cambia esto a la contraseña de tu cuenta de correo electrónico.