import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # EMLAK++

SECRET_KEY = 'p$kq#3mc2bnl*^yx-5!=6+9xg9di40=4kvknlh*v9acfq&fujb'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages.apps.PagesConfig',  # uygulamamızı kayıt ettik
    'listings.apps.ListingsConfig',
    'realtors.apps.RealtorsConfig',
    'django.contrib.humanize', # template üzerinde sayıları daha hoş göstermek için kullanılır
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

ROOT_URLCONF = 'emlakplus.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # ana dizindeki templates klasörü dedik
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

WSGI_APPLICATION = 'emlakplus.wsgi.application'

DATABASES = {
    'default': {
        # pip install psycopg2  -> postgresql bağlantısı için
        'ENGINE': 'django.db.backends.postgresql',  # postgresql için gerekli ayarlarımızı yapıyoruz
        'NAME': 'emlakplus',
        'USER': 'postgres',
        'PASSWORD': 'cokzorsifre',
        'HOST': 'localhost'
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

LANGUAGE_CODE = 'tr'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # collect static yapınca buraya toplanacak. manage.py yanına
STATICFILES_DIRS = [  # app'ler buradan staticleri çekecek. Yani template'ler
    os.path.join(BASE_DIR, 'emlakplus/static')
]

# Media Dosyaları İçin Ayarlar
# 1-) pip install pillow
# 2-) settings.py içerisinde media ayarlarını yap
# 3-) base urls.py içerisine +static yap
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # ana dizinde media klasörü altına. manage.py yanına
MEDIA_URL = '/media/' # src kısmına 'static' yazdığımız gibi media yazacağımız için