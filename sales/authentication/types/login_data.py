from django.contrib.auth.password_validation import validate_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from dataclasses import dataclass

from core.abstract import Params


@dataclass
class LogInData(Params):
    email: str
    password: str

    def validate(self) -> None:
        errors = {}

        errors["email"] = self._validate_email()
        errors["password"] = self._validate_password()

        self._raise_errors(errors)
    
    def _validate_email(self) -> list:
        errors = []

        if self.email:
            try:
                validate_email(self.email)
            except ValidationError as e:
                errors += e.messages
        else:
            errors.append("Поле обязятельно для заполнения")
        
        return errors
        
    def _validate_password(self) -> list:
        errors = []

        if self.password:
            try:
                validate_password(self.password)
            except ValidationError as e:
                errors += e.messages
        else:
            errors.append("Поле обязятельно для заполнения")
        
        return errors