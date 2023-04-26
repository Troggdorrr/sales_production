from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

from dataclasses import dataclass
from uuid import UUID

from core.abstract import Params


@dataclass
class ChangePasswordData(Params):
    uuid: str
    password: str

    def validate(self) -> None:
        errors = {}

        errors["uuid"] = self._validate_uuid()
        errors["password"] = self._validate_password()

        self._raise_errors(errors)
    
    def _validate_uuid(self) -> list:
        errors = []
        if self.uuid:
            try:
                UUID(self.uuid)
            except ValueError:
                errors.append("Неправильный формат")
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