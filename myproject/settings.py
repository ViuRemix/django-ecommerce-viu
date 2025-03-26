"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 5.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u2^2j$3nzy=&4bx9!v5yf06o9#eejurpxis%n!d^zmtj^88ldf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ecommerce',
    'widget_tweaks',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR,'templates'],
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

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# chuyển hình ảnh để gọn hơn


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# STATIC (file tĩnh)
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'ecommerce', 'static'),
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# MEDIA (file upload)
MEDIA_URL = '/media/'  
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# CHỖ NÀY LÀ CSS CHO APP JAZZMIN
# css màu cho  JAZZMIN 
JAZZMIN_UI_TWEAKS = {
    "theme": "flatly",  # Chọn theme có sẵn: 'darkly', 'flatly', 'cyborg', 'superhero', v.v.
    "navbar_small_text": False,  # Chữ nhỏ trên thanh navbar
    "body_small_text": False,  # Chữ nhỏ trên toàn bộ trang
    "brand_colour": "navbar-dark bg-primary",  # Màu nền của brand
    "accent": "primary",  # Màu chính của giao diện
    "navbar": "navbar-dark navbar-primary",  # Màu của navbar
    "no_navbar_border": True,  # Ẩn đường viền navbar
    "sidebar_nav_compact_style": True,  # Sidebar nhỏ gọn
}
# sửa cài đặt
JAZZMIN_SETTINGS = {
    "site_title": "Quản lý hệ thống",  # Tiêu đề tab trình duyệt
    "site_header": "Trang quản trị",  # Tiêu đề hiển thị trên thanh trên cùng
    "site_brand": "Quản trị viên",  # Chữ ở góc trái thanh điều hướng
    "welcome_sign": "Chào mừng đến với trang quản trị",  # Chữ trên trang đăng nhập
    "site_logo": "images/logo_viu.png",  # Logo hiển thị ở góc trên trái
    "login_logo": "images/logo_viu.png",  # Logo hiển thị trên trang đăng nhập
    "login_logo_dark": "images/logo_dark.png",  # Logo hiển thị khi bật chế độ tối
    "copyright": "© 2025 Quản lý hệ thống. All rights reserved.",  # Bản quyền
    "user_avatar": "profile_picture",  # Thuộc tính của User chứa avatar
}


# login 

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/login/'

