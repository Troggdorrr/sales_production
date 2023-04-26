from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

from dataclasses import dataclass

from core.abstract import Params


@dataclass
class LogOutData(Params):
    refresh: str

    def validate(self) -> None:
        errors = {}

        errors["refresh"] = self._validate_refresh_token()
        
        self._raise_errors(errors)
    
    def _validate_refresh_token(self) -> list:
        errors = []

        if self.refresh:
            try:
                RefreshToken(self.refresh)
            except TokenError:
                errors.append("Неизвестный токен")
        else:
            errors.append("Поле обязятельно для заполнения")
        
        return errors