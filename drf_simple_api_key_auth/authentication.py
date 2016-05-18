from django.contrib.auth import get_user_model
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

from . import settings


class SimpleApiKeyAuthentication(TokenAuthentication):
    """
    Simple token based authentication. This should only be used by internal web
    services. Clients should authenticate by passing the token key in the
    "Authorization" HTTP header, prepended with the string "Key ".
    For example:
        Authorization: Key 401f7ac837da42b97f613d789819ff93537bee6a
    """
    keyword = 'Key'

    def _get_user(self):
        UserModel = get_user_model()

        user, created = UserModel.objects.get_or_create(
            username=settings.USERNAME,
            email=settings.EMAIL,
            is_superuser=True,
        )
        
        if created:
            user.set_unusable_password()
            user.save()

        return user

    def authenticate_credentials(self, key):
        if key not in settings.API_KEYS:
            raise AuthenticationFailed('Invalid key')
        
        user = self._get_user()
        return user, key
