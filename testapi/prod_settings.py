import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = '+#ry@y*1u1sm^zdv(fw17m#!2!)j(qn4y@q7@7*!sg7gd8+h2a'


DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "84.201.170.122"]


DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.postgresql_psycopg2',
         'NAME': 'ezop',
         'USER': 'yunis',
         'PASSWORD': '123456',
         'HOST': 'localhost',
         'PORT': '5432',
     }
 }


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
