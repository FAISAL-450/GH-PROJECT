import os
import json
from pathlib import Path

# 🏗️ Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 Security
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'unsafe-default-key')
DEBUG = os.environ.get('DJANGO_DEBUG', 'False') == 'True'

# 🌍 Hosts and CSRF
try:
    ALLOWED_HOSTS = json.loads(os.environ.get('DJANGO_ALLOWED_HOSTS', '["localhost", "127.0.0.1"]'))
except json.JSONDecodeError:
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

try:
    CSRF_TRUSTED_ORIGINS = json.loads(os.environ.get('CSRF_TRUSTED_ORIGINS', '[]'))
except json.JSONDecodeError:
    CSRF_TRUSTED_ORIGINS = []

# 📦 Installed apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Project apps
    'construction_department',
    'sales_department',
    'project',
    'customer',
    'home.apps.HomeConfig',
    'azure_auth',
]

AZURE_AUTH = {
    "CLIENT_ID": os.getenv("AZURE_CLIENT_ID"),
    "CLIENT_SECRET": os.getenv("AZURE_CLIENT_SECRET"),
    "REDIRECT_URI": os.getenv("AZURE_REDIRECT_URI"),
    "SCOPES": ["User.Read", "GroupMember.Read.All"],
    "AUTHORITY": os.getenv("AZURE_AUTHORITY"), 
    "USERNAME_ATTRIBUTE": "preferred_username",
    "ROLES": {
        "f2a25025-19e6-427f-a8ce-db6224097658": "Construction",
        "75c3c3ff-3372-47a6-923e-bda304e98f6f": "Sales"
    }
}

LOGIN_URL = "/azure_auth/login"
LOGIN_REDIRECT_URL = "/"

# ⚙️ Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware' if not DEBUG else '',  # Enable in production
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
MIDDLEWARE = [mw for mw in MIDDLEWARE if mw]  # Remove empty string if DEBUG

# 🌐 Root URLs and WSGI
ROOT_URLCONF = 'gh_garden.urls'
WSGI_APPLICATION = 'gh_garden.wsgi.application'

# 🎨 Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

# 🗄️ Database (switchable via env if needed)
DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': os.environ.get('DB_NAME', BASE_DIR / 'db.sqlite3'),
    }
}

# 🔒 Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 🌍 Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Dhaka'
USE_I18N = True
USE_TZ = True

# 📁 Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Production static file handling
if not DEBUG:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# 🆔 Default primary key field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

