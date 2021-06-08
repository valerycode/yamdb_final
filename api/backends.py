from rest_framework import authentication

from .models.user_confirm_code_db import UserConfirmCodeDb


class ConfirmUserRegistrationAuthentication(authentication.BaseAuthentication):
    """Аутентификация будущего пользователя."""
    def authenticate(self, request, email=None, confirm_code=None):
        user = UserConfirmCodeDb.objects.get(
            email=email, confirm_code=confirm_code)
        try:
            user
        except UserConfirmCodeDb.DoesNotExist:
            return None
        return user
