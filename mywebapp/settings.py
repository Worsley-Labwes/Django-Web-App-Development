import os
import dj_database_url
from pathlib import Path

# Base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Secret key for security (change it for production)
SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key')

# Debug mode (set to True only in development)
DEBUG = True  # Change to False in production

# Allowed hosts for deployment
ALLOWED_HOSTS = ['your-username.pythonanywhere.com', 'your-app.onrender.com', '127.0.0.1', 'localhost', '.onrender.com']

# Installed apps, including Django admin
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main',  # Your main Django app
]
ROOT_URLCONF = 'mywebapp.urls'

# Middleware (Fixes missing session/authentication errors)
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Required
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Required
    'django.contrib.messages.middleware.MessageMiddleware',  # Required
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Database configuration (uses SQLite by default)
DATABASES = {
    'default': dj_database_url.config(default=os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3'))
}
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default="postgres://user:password@hostname:port/dbname")
}


# Templates configuration (Fixes admin panel issues)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "main/templates"],  # Ensure the correct path is set
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


# Static files configuration
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Authentication redirects
LOGIN_REDIRECT_URL = 'dashboard'
LOGOUT_REDIRECT_URL = 'login'

# Fixes AutoField warning in models
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
