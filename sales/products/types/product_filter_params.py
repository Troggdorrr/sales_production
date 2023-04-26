from dataclasses import dataclass
from typing import Optional

from core.abstract import Params

from products.enums import ProductSortBy


@dataclass
class ProductFilterParams(Params):
    price__lt: Optional[int] = None
    price__gt: Optional[int] = None
    is_expired: Optional[bool] = None
    promo_type: Optional[int] = None
    city: Optional[int] = None
    donor: Optional[int] = None
    sort_by: Optional[ProductSortBy] = None
    search: Optional[str] = None

    def validate(self) -> None:
        errors = {}

        errors["price__lt"] = self._validate_price(self.price__lt)
        errors["price__gt"] = self._validate_price(self.price__gt)
        errors["is_expired"] = self._validate_is_expired()
        errors["promo_type"] = self._validate_promo_type()
        errors["city"] = self._validate_city()
        errors["donor"] = self._validate_donor()
        errors["sort_by"] = self._validate_sort_by()
        errors["search"] = self._validate_search()

        if (
            not errors.get("price__gt")
            and not errors.get("price__lt")
            and not self._is_valid_prices_range()
        ):
            errors["price__lt"] = ["Некорректный диапозон"]
            errors["price__gt"] = ["Некорректный диапозон"]

        self._raise_errors(errors)

    def _validate_price(self, price: int) -> list:
        errors = []

        if price:
            try:
                int(price)
            except ValueError:
                errors.append("Цена должна быть указана числом")

        return errors

    def _is_valid_prices_range(self) -> bool:
        if (self.price__lt and self.price__gt) and (
            int(self.price__lt) < int(self.price__gt)
        ):
            return False
        return True

    def _validate_is_expired(self) -> list:
        errors = []

        if self.is_expired:
            if self.is_expired not in ["true", "false"]:
                errors.append("Некорректное значение (Доступны: true, false)")
            else:
                self.is_expired = True if self.is_expired == "true" else False

        return errors

    def _validate_city(self) -> list:
        errors = []

        if self.city:
            try:
                self.city = int(self.city)
            except ValueError:
                errors.append("Должен быть указан числовой номер")

        return errors

    def _validate_donor(self) -> list:
        errors = []

        if self.donor:
            try:
                self.donor = int(self.donor)
            except ValueError:
                errors.append("Должен быть указан числовой номер")

        return errors

    def _validate_promo_type(self) -> list:
        errors = []

        if self.promo_type:
            try:
                self.promo_type = int(self.promo_type)
            except ValueError:
                errors.append("Должен быть указан числовой номер")

        return errors

    def _validate_sort_by(self) -> list:
        errors = []

        if self.sort_by:
            if not ProductSortBy.has(self.sort_by):
                errors.append("Недопустимое значение")

        return errors

    def _validate_search(self) -> list:
        errors = []

        if self.search:
            if len(self.search) < 3:
                errors.append("Слишком короткий запрос")

        return errors