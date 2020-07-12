"""
Django settings for introdesign project.

Generated by 'django-admin startproject' using Django 3.0.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import cloudinary
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "z5m0-$p25zosfk9^!fa^+#%^xk$k)!)m=*y2^r5#aes=bnsdyi"


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['thevillageapp.herokuapp.com', 'localhost', '*']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # The following apps are required
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django.contrib.staticfiles',
    'cloudinary_storage',
    'autoslug',
    'ckeditor',
    'service',
    'events',
    'plans',
    'cloudinary',
    'blog',
    'accounts',
    'phone_field',
    'django_smtp_ssl',
    'taggit',
    'tinymce',
    'schedule',
    'celery',
    'background_task',
    'apscheduler',
    'redis',
    

]
#configure cloudinary
cloudinary.config(
    cloud_name = os.environ["CLOUD_NAME"],
    api_key = os.environ["API_KEY"],
    api_secret = os.environ["API_SECRET"],
    secure = True)

    
# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME':os.environ["CLOUD_NAME"],
#     'API_KEY': os.environ["API_KEY"],
#     'API_SECRET': os.environ["API_SECRET"]
# }


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'introdesign.urls'

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

WSGI_APPLICATION = 'introdesign.wsgi.application'
LOGIN_REDIRECT_URL = '/'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     # 'default': {
#     #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
#     #     'NAME': 'thevillage',
#     #     'USER': 'admin',
#     #     'PASSWORD': 'thevillage',
#     #     'HOST': 'localhost',
#     #     'PORT': '',
#     # }
#     'default': dj_database_url.config()
# }

#     #  'default': {
#     #     'ENGINE': 'django.db.backends.sqlite',
#     #     'NAME': 'xe',
#     #     'USER': 'a_user',
#     #     'PASSWORD': 'a_password',
#     #     'HOST': '',
#     #     'PORT': '',
#     # }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'accounts.Account'

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Brazzaville'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
MEDIA_URL = '/media/'  # or any prefix you choose
# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
MEDIA_ROOT  = os.path.join(BASE_DIR, 'media')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',

    'allauth.account.auth_backends.AuthenticationBackend',
)
#TinyMCE Configurations
TINYMCE_DEFAULT_CONFIG = {
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
    }

SITE_ID = 1

#SMTP Configuration
EMAIL_BACKEND = 'django_smtp_ssl.SSLEmailBackend'
EMAIL_HOST = 'twentytwo.qservers.net'
EMAIL_PORT = 465
EMAIL_USE_TLS = True
Email_USE_SSL = True
EMAIL_HOST_USER = 'booking@village.ng'
EMAIL_HOST_PASSWORD = 'thevillagebooking'

# EMAIL_BACKEND = os.environ['EMAIL_BACKEND']
# EMAIL_HOST = os.environ['EMAIL_HOST']
# EMAIL_PORT = os.environ['EMAIL_PORT']
# EMAIL_USE_TLS = False
# EMAIL_USE_SSL = os.environ['Email_USE_SSL']
# EMAIL_HOST_USER = os.environ['EMAIL_HOST_USER']
# EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD']

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'maduabuchiokonkwo@gmail.com'
# EMAIL_HOST_PASSWORD = 'Bigdata11051989'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.elasticemail.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = 'maduabuchiokonkwo@village.ng'
# EMAIL_HOST_PASSWORD = '46A11417A4240B8A2F9AA5883D3119165A8A'

# CELERY_BROKER_URL = 'redis://h:p36bcfacf7bdb4b6efc96c69f61c031afd7f672dd4734f7583219b91420e86ae0@ec2-52-70-215-224.compute-1.amazonaws.com:30099'
# CELERY_ACCEPT_CONTENT = ['json']
# CELERY_TASK_SERIALIZER = 'json'