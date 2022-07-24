import os
from .settings import *

DEBUG = True

SECRET_KEY = 'posagjaspogajspogaspojhgjpoas251p5j21p5j12p5o21j'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}