# -*- encoding: utf-8 -*-

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import django
import os
import sys

from django.conf import settings
from django.core.management import execute_from_command_line


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.abspath(os.path.join(BASE_DIR, '..')))

CUSTOM_INSTALLED_APPS = (
    'django_extensions',
    'powerdns',
    'rest_framework',
    'django_powerdns_api',
)
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


settings.configure(
    SECRET_KEY="secret_key",
    DEBUG=False,
    TEMPLATE_DEBUG=False,
    ALLOWED_HOSTS=[],
    INSTALLED_APPS=INSTALLED_APPS + CUSTOM_INSTALLED_APPS,
    MIDDLEWARE_CLASSES=MIDDLEWARE_CLASSES,
    ROOT_URLCONF='django_powerdns_api.urls',
    DATABASES={
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': ':memory:',
        }
    },
    LANGUAGE_CODE='en-us',
    TIME_ZONE='UTC',
    USE_I18N=True,
    USE_L10N=True,
    USE_TZ=True,
    STATIC_URL='/static/',
    PASSWORD_HASHERS=(
        'django.contrib.auth.hashers.MD5PasswordHasher',
    ),
)

django.setup()

args = [sys.argv[0], 'test']
test_cases = '.'
offset = 1
try:
    sys.argv[1]
except IndexError:
    pass
else:
    option = sys.argv[1].startswith('-')
    if not option:
        test_cases = sys.argv[1]
        offset = 2
args.append(test_cases)
args.append('--verbosity=2')
args.extend(sys.argv[offset:])

execute_from_command_line(args)
