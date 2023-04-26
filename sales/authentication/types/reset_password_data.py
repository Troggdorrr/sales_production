from dataclasses import dataclass

from core.abstract import Params


@dataclass
class ResetPasswordData(Params):
    identifier: str

    def validate(self) -> None:
        errors = {}
        errors["identifier"] = self._validate_identifier()
        self._raise_errors(errors)
    
    def _validate_identifier(self) -> list:
        errors = []
        if not self.identifier:
            errors.append("Поле обязятельно для заполнения") 
        return errors
