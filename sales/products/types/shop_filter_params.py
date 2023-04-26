from dataclasses import dataclass
from typing import Optional

from core.abstract import Params


@dataclass
class ShopFilterParams(Params):
    city: Optional[int] = None

    def validate(self) -> None:
        errors = {}

        errors["city"] = self._validate_city()
        
        self._raise_errors(errors)
    
    def _validate_city(self) -> list:
        errors = []

        if self.city:
            try:
                self.city = int(self.city)
            except ValueError:
                errors.append("Должен быть указан числовой номер")

        return errors