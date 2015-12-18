from logan.runner import run_app, configure_app
from django.utils.crypto import get_random_string


def generate_secret_key():
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return get_random_string(50, chars)


CONFIG_TEMPLATE = '''
"""
This configuration file is just Python code. You may override any global
defaults by specifying them here.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
from strongpoc.conf.settings import *

import os.path

# Path where the config is found.
CONF_ROOT = os.path.dirname(__file__)

# A boolean that turns on/off debug mode. Never deploy a site into production
# with DEBUG turned on.
# Default: False
DEBUG = False

ALLOWED_HOSTS = ["*"]

############
# Database #
############
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(CONF_ROOT, 'strongpoc.sqlite3'),
        'USER': 'strongpoc',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

############
# Security #
############

# A URL-safe base64-encoded 32-byte key. This must be kept secret. Anyone with
# this key is able to create and read messages. This key is used for
# encryption/decryption of sessions and auth tokens.
SECRET_KEY = %(secret_key)r
'''


def generate_settings(config_template=None):
    """Used to emit a config template."""
    if config_template is None:
        config_template = CONFIG_TEMPLATE.strip()

    secret_key = generate_secret_key()
    return config_template % dict(secret_key=secret_key)


def main():
    """CLI application used to manage NSoT."""
    run_app(
        project='strongpoc',
        default_config_path='~/.strongpoc/strongpoc.conf.py',
        default_settings='strongpoc.conf.settings',
        settings_initializer=generate_settings,
        settings_envvar='STRONGPOC_CONF',
        # initializer=initialize_app,
    )