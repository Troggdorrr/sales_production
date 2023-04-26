from django.db.models import QuerySet

from products.types import ShopFilterParams


class ShopFilter:
    def __init__(self, queryset: QuerySet, params: ShopFilterParams) -> None:
        self._queryset = queryset
        self._params = params

    @property
    def queryset(self) -> QuerySet:
        return self._queryset

    def filter(self) -> None:
        if self._params.city:
            self._filter_by_city()
 
    def _filter_by_city(self) -> None:
        self._queryset = self._queryset.filter(city__id=self._params.city)

    def sort(self) -> None:
        self._queryset = self._queryset.order_by("id")