import os
from dotenv import load_dotenv


load_dotenv()
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/



# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False


DATABASES = {
    'default': {
        'ENGINE': os.getenv('DATABASE_ENGINE'),
        'NAME': os.getenv('DATABASE_NAME'),
        'USER':os.getenv('DATABASE_USER'),
        'PASSWORD':os.getenv('DATABASE_PASSWORD'),
        'HOST':os.getenv('DATABASE_HOST'),
        'PORT':os.getenv('DATABASE_PORT'),
	    'TEST': {
		   'NAME' : os.getenv('DATABASE_TESTNAME'),
	    }
    }
}

STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'