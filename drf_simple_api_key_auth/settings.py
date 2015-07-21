from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

USERNAME = getattr(settings, 'REST_FRAMEWORK_SIMPLE_AUTH_USER_USERNAME', 'simple_api_user')
EMAIL = getattr(settings, 'REST_FRAMEWORK_SIMPLE_AUTH_USER_EMAIL', 'simple_api_user@example.com')

try:
    API_KEYS = settings.REST_FRAMEWORK_SIMPLE_AUTH_KEYS
except AttributeError:
    raise ImproperlyConfigured('REST_FRAMEWORK_SIMPLE_AUTH_KEYS not defined in django settings')
