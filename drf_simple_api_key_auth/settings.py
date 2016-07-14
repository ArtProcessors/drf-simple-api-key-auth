from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

USER_KWARGS = getattr(settings, 'REST_FRAMEWORK_SIMPLE_AUTH_USER_KWARGS', {
    'username': 'simple_api_user',
    'email': 'simple_api_user@example.com',
    'is_superuser': True,
})

try:
    API_KEYS = settings.REST_FRAMEWORK_SIMPLE_AUTH_KEYS
except AttributeError:
    raise ImproperlyConfigured('REST_FRAMEWORK_SIMPLE_AUTH_KEYS not defined in django settings')
