from django.db.models import QuerySet

from products.types import SimiliarFilterParams, ProductFilterParams

from .product_filter import ProductFilter


class SimiliarFilter:
    def __init__(self, queryset: QuerySet, params: SimiliarFilterParams) -> None:
        self._queryset = queryset
        self._params = params

    @property
    def queryset(self) -> QuerySet:
        return self._queryset

    def filter(self) -> None:
        params = ProductFilterParams(
            city=self._params.city, is_expired=self._params.is_expired
        )
        filter_service = ProductFilter(self._queryset, params)
        filter_service.filter()
        self._queryset = filter_service.queryset

    def sort(self) -> None:
        self._queryset = self._queryset.order_by("similarity")
