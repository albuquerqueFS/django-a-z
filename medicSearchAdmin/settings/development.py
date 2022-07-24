import os
from .settings import *

DEBUG = true

# secret key do ambiente de dev
SECRET_KEY = 'pasj4oapsjpo2j51powjo12h5o12i521'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}