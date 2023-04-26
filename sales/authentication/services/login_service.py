from django.contrib.auth import get_user_model, authenticate

from authentication.types import LogInData, JwtAuth
from authentication.errors import InvalidLoginData

from .token_service import TokenService


User = get_user_model()


class LoginService:
    def __init__(self, data: LogInData) -> None:
        self._data = data

    def login(self) -> JwtAuth:
        user = self._get_user()
        tokens = self._get_tokens(user)
        return tokens
    
    def _get_user(self) -> User:
        user = authenticate(username=self._data.email, password=self._data.password)
        if user:
            return user
        else:
            raise InvalidLoginData
    
    def _get_tokens(self, user: User) -> JwtAuth:
        return TokenService.create_tokens(user)