from dataclasses import dataclass
from typing import Optional

from core.abstract import Params

from products.enums import CitySortBy


@dataclass
class CityFilterParams(Params):
    sort_by: Optional[CitySortBy] = None
    search: Optional[str] = None

    def validate(self) -> None:
        errors = {}

        errors["sort_by"] = self._validate_sort_by()
        errors["search"] = self._validate_search()
        
        self._raise_errors(errors)

    def _validate_sort_by(self) -> list:
        errors = []

        if self.sort_by:
            if not CitySortBy.has(self.sort_by):
                errors.append("Недопустимое значение")

        return errors
    
    def _validate_search(self) -> list:
        errors = []

        if self.search:
            if len(self.search) < 3:
                errors.append("Слишком короткий запрос")

        return errors
