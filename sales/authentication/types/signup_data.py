from django.core.exceptions import ObjectDoesNotExist

from rest_framework.exceptions import ValidationError

from dataclasses import dataclass
import re

from users.services import UserCRUD

from .login_data import LogInData


@dataclass
class SignUpData(LogInData):
    username: str

    def validate(self) -> None:
        errors = {}

        try:
            super().validate()
        except ValidationError as e:
            errors = e.detail

        errors["username"] = self._validate_username()
        
        self._raise_errors(errors)
    
    def _validate_email(self) -> list:
        errors = super()._validate_email()
        if self.email:
            try:
                UserCRUD.get_by_email(self.email)
                errors.append("Пользователь с такой почтой уже существует")
            except ObjectDoesNotExist:
                pass
        return errors

    def _validate_username(self) -> list:
        errors = []

        if self.username:
            if not re.match("[0-9a-zA-Zа-яА-Я_]{3,16}$", self.username):
                errors.append("Неправильный формат")
            try:
                UserCRUD.get_by_username(self.username)
                errors.append("Пользователь с таким именем уже существует")
            except ObjectDoesNotExist:
                pass
        else:
            errors.append("Поле обязятельно для заполнения")

        return errors