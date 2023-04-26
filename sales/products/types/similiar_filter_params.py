from dataclasses import dataclass
from typing import Optional

from core.abstract import Params


@dataclass
class SimiliarFilterParams(Params):
    city: Optional[int] = None
    is_expired: Optional[bool] = None

    def validate(self) -> None:
        errors = {}

        errors["city"] = self._validate_city()
        errors["is_expired"] = self._validate_is_expired()
        
        self._raise_errors(errors)
    
    def _validate_city(self) -> list:
        errors = []

        if self.city:
            try:
                self.city = int(self.city)
            except ValueError:
                errors.append("Должен быть указан числовой номер")

        return errors
    
    def _validate_is_expired(self) -> list:
        errors = []

        if self.is_expired:
            if self.is_expired not in ["true", "false"]:
                errors.append("Некорректное значение (Доступны: true, false)")
            else:
                self.is_expired = True if self.is_expired == "true" else False

        return errors
