from linkstash.settings.main import *



DEBUG = False


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'live_db.sqlite3'),
    }
}

