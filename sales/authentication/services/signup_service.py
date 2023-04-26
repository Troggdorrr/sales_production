from django.contrib.auth import get_user_model

from authentication.types import SignUpData, JwtAuth
from authentication.tasks import send_success_signup_email

from .token_service import TokenService


User = get_user_model()


class SignUpService:
    def __init__(self, data: SignUpData) -> None:
        self._data = data

    def signup(self) -> JwtAuth:
        user = self._get_user()
        tokens = self._get_tokens(user)
        self._do_tasks(user.pk)
        return tokens
    
    def _get_user(self) -> User:
        return User.objects.create_user(
            username=self._data.username,
            email=self._data.email,
            password=self._data.password,
        )
    
    def _get_tokens(self, user: User) -> JwtAuth:
        return TokenService.create_tokens(user)
    
    def _do_tasks(self, user_pk: int) -> None:
        send_success_signup_email.delay(user_pk)
