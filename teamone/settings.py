"""
Django settings for teamone project.

Generated by 'django-admin startproject' using Django 2.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "q4!d06oj_jy(1$q#@*&0bcnn4*ub*)0#5n9^p*hp+3#5)tb2(+"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["uplyft.herokuapp.com", "localhost", "127.0.0.1", "testserver"]

# Creating a custom user model
LOGIN_URL = "/candidate_login/"
AUTH_USER_MODEL = "uplyft.CustomUser"
# This should be the dashboard
LOGIN_REDIRECT_URL = "uplyft:index"
LOGOUT_REDIRECT_URL = ""

# Application definition
INSTALLED_APPS = [
    "localflavor",
    "crispy_forms",
    "phonenumber_field",
    "uplyft.apps.UplyftConfig",
    "register.apps.RegisterConfig",
    "apply.apps.ApplyConfig",
    "applications.apps.ApplicationsConfig",
    "candidate_login.apps.CandidateLoginConfig",
    "candidate_profile.apps.CandidateProfileConfig",
    "employer_login.apps.EmployerLoginConfig",
    "jobs.apps.JobsConfig",
    "password_reset.apps.PasswordResetConfig",
    "dashboard.apps.DashboardConfig",
    "department_details.apps.DepartmentDetailsConfig",
    "department_profile.apps.DepartmentProfileConfig",
    "errors.apps.ErrorsConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.humanize",
    "django.contrib.staticfiles",
    "widget_tweaks",
    "django_filters",
    "file_resubmit",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "storages",
]

SITE_ID = 2

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "teamone.urls"

CACHES = {
    "default": {"BACKEND": "django.core.cache.backends.locmem.LocMemCache"},
    "file_resubmit": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": "/tmp/file_resubmit/",
    },
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
            ]
        },
    }
]

WSGI_APPLICATION = "teamone.wsgi.application"

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth."
        + "password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/New_York"
CRISPY_TEMPLATE_PACK = "bootstrap4"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(PROJECT_DIR, "static")
STATIC_URL = "/static/"
if "HOME" in os.environ and "/app" in os.environ["HOME"]:
    django_heroku.settings(locals())

# Email settings
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_USERNAME_REQUIRED = False

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "uplyft1234@gmail.com"
EMAIL_HOST_PASSWORD = "mwwymvtlbxnluvqx"
DEFAULT_FROM_EMAIL = "Uplyft Team <noreply@uplyft.com>"

# Google authentication Client-ID and Secret key
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = (
    "458803488859-vf1pli732quc9m9n0nbpbggehj5gomrf.apps.googleusercontent.com"
)
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "M1y9_Z-jNwqArncabT7_zZWV"

AWS_ACCESS_KEY_ID = "AKIA46VH6MQWFGIZCO5M"
AWS_SECRET_ACCESS_KEY = "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"
AWS_STORAGE_BUCKET_NAME = "uplyft-s3"
AWS_S3_CUSTOM_DOMAIN = "%s.s3.amazonaws.com" % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=600"}
# AWS_LOCATION = 'static'

# AWS_DEFAULT_ACL = None

MEDIA_URL = "/media/"
DEFAULT_FILE_STORAGE = "uplyft.s3_storage.ResumeStorage"
