"""
These settings are here to use during tests, because django requires them.

In a real-world use case, apps in this project are installed into other
Django applications, so these settings will not be used.
"""

from os.path import abspath, dirname, join
# from survey.tests import _mock_third_party_modules

import sys
from unittest.mock import Mock

mock_openedx = Mock()

# Mock 'openedx.core.djangolib.markup.HTML'
mock_openedx.core.djangolib.markup.HTML = Mock()

# Mock 'openedx.core.djangoapps.user_api.accounts.signals'
mock_openedx.core.djangoapps.user_api.accounts = Mock()
mock_openedx.core.djangoapps.user_api.accounts.signals = Mock()

# Mock 'USER_RETIRE_LMS_MISC'
mock_openedx.core.djangoapps.user_api.accounts.signals.USER_RETIRE_LMS_MISC = Mock()

# Mock 'openedx.core.djangoapps.user_api.accounts.tests.retirement_helpers.fake_completed_retirement'
mock_openedx.core.djangoapps.user_api.accounts.tests = Mock()
mock_openedx.core.djangoapps.user_api.accounts.tests.retirement_helpers = Mock()
mock_openedx.core.djangoapps.user_api.accounts.tests.retirement_helpers.fake_completed_retirement = Mock()

# Mock 'xmodule.modulestore.tests.django_utils.ModuleStoreTestCase'
mock_xmodule = Mock()
mock_xmodule.modulestore = Mock()
mock_xmodule.modulestore.tests = Mock()
mock_xmodule.modulestore.tests.django_utils = Mock()
mock_xmodule.modulestore.tests.django_utils.ModuleStoreTestCase = Mock()

# Mock 'xmodule.modulestore.tests.factories.CourseFactory'
mock_xmodule.modulestore.tests.factories = Mock()
mock_xmodule.modulestore.tests.factories.CourseFactory = Mock()

# Register mocks in sys.modules
sys.modules["openedx"] = mock_openedx
sys.modules["openedx.core"] = mock_openedx.core
sys.modules["openedx.core.djangolib"] = mock_openedx.core.djangolib
sys.modules["openedx.core.djangolib.markup"] = mock_openedx.core.djangolib.markup
sys.modules["openedx.core.djangolib.markup.HTML"] = mock_openedx.core.djangolib.markup.HTML

sys.modules["openedx.core.djangoapps"] = mock_openedx.core.djangoapps
sys.modules["openedx.core.djangoapps.user_api"] = mock_openedx.core.djangoapps.user_api
sys.modules["openedx.core.djangoapps.user_api.accounts"] = mock_openedx.core.djangoapps.user_api.accounts
sys.modules[
    "openedx.core.djangoapps.user_api.accounts.signals"] = mock_openedx.core.djangoapps.user_api.accounts.signals
sys.modules["openedx.core.djangoapps.user_api.accounts.tests"] = mock_openedx.core.djangoapps.user_api.accounts.tests
sys.modules[
    "openedx.core.djangoapps.user_api.accounts.tests.retirement_helpers"] = mock_openedx.core.djangoapps.user_api.accounts.tests.retirement_helpers

sys.modules["xmodule"] = mock_xmodule
sys.modules["xmodule.modulestore"] = mock_xmodule.modulestore
sys.modules["xmodule.modulestore.tests"] = mock_xmodule.modulestore.tests
sys.modules["xmodule.modulestore.tests.django_utils"] = mock_xmodule.modulestore.tests.django_utils
sys.modules["xmodule.modulestore.tests.factories"] = mock_xmodule.modulestore.tests.factories


def root(*args):
    """
    Get the absolute path of the given path relative to the project root.
    """
    return join(abspath(dirname(__file__)), *args)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'default.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.sessions',
    'survey',
)

LOCALE_PATHS = [
    root('survey', 'conf', 'locale'),
]

ROOT_URLCONF = 'survey.urls'

SECRET_KEY = 'insecure-secret-key'

MIDDLEWARE = (
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
)

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'APP_DIRS': False,
    'OPTIONS': {
        'context_processors': [
            'django.contrib.auth.context_processors.auth',  # this is required for admin
            'django.contrib.messages.context_processors.messages',  # this is required for admin
        ],
    },
}]

ALLOWED_HOSTS  = ['*']