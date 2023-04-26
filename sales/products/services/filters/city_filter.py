from django.db.models import QuerySet

from products.types import CityFilterParams


class CityFilter:
    def __init__(self, queryset: QuerySet, params: CityFilterParams) -> None:
        self._queryset = queryset
        self._params = params

    @property
    def queryset(self) -> QuerySet:
        return self._queryset

    def filter(self) -> None:
        if self._params.search:
            self._filter_by_search()

    def _filter_by_search(self) -> None:
        self._queryset = self._queryset.filter(name__icontains=self._params.search)

    def sort(self) -> None:
        if self._params.sort_by:
            self._queryset = self._queryset.order_by(self._params.sort_by)
        else:
            self._queryset = self._queryset.order_by("id")
