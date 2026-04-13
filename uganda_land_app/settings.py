import os
from pathlib import Path

# 1. ESSENTIAL PATH & SECURITY SETTINGS
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-cornycom-key-replace-this-later'

# KEEP True for now to see errors; change to False when site is 100% ready
DEBUG = True

# Add your Render URL here once you create the service
ALLOWED_HOSTS = ['*', 'cornycom-backend.onrender.com', 'localhost', '127.0.0.1']

# 2. YOUR INSTALLED APPS
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'listings',
]

# 3. YOUR MIDDLEWARE
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Added for Render static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'uganda_land_app.urls'
WSGI_APPLICATION = 'uganda_land_app.wsgi.application'

# 4. YOUR TEMPLATES
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# 5. YOUR DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 6. YOUR CORS SETTINGS
CORS_ALLOW_ALL_ORIGINS = True

# Standard Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Africa/Kampala' # Updated for Uganda
USE_I18N = True
USE_TZ = True

# 7. STATIC & MEDIA FILES (Crucial for Hosting)
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles' # Added for Render
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'