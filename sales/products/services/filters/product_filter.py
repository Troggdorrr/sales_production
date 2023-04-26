from django.db.models import (
    QuerySet,
    F,
    FloatField,
    ExpressionWrapper,
    OuterRef,
    Exists,
)
from django.utils import timezone
from django.contrib.postgres.search import SearchQuery

from products.types import ProductFilterParams
from products.enums import ProductSortBy
from products.models import City


class ProductFilter:
    def __init__(self, queryset: QuerySet, params: ProductFilterParams) -> None:
        self._queryset = queryset
        self._params = params

    @property
    def queryset(self) -> QuerySet:
        return self._queryset

    def filter(self) -> None:
        if self._params.price__lt or self._params.price__gt:
            self._filter_by_price()
        if self._params.is_expired is not None:
            self._filter_by_is_expired()
        if self._params.promo_type:
            self._filter_by_promo_type()
        if self._params.city:
            self._filter_by_city()
        if self._params.donor:
            self._filter_by_donor()
        if self._params.search:
            self._filter_by_search()

    def _filter_by_price(self) -> None:
        if self._params.price__lt:
            self._queryset = self._queryset.filter(
                promo_price__lt=self._params.price__lt,
            )
        if self._params.price__gt:
            self._queryset = self._queryset.filter(
                promo_price__gt=self._params.price__gt,
            )

    def _filter_by_is_expired(self) -> None:
        if self._params.is_expired:
            self._queryset = self._queryset.filter(promo__date_end__lt=timezone.now())
        else:
            self._queryset = self._queryset.filter(promo__date_end__gte=timezone.now())

    def _filter_by_promo_type(self) -> None:
        self._queryset = self._queryset.filter(promo__type__id=self._params.promo_type)

    def _filter_by_city(self) -> None:
        self._queryset = self._queryset.filter(
            Exists(
                City.objects.filter(
                    shops__product__id=OuterRef("pk"), id=self._params.city
                )
            )
        )

    def _filter_by_donor(self) -> None:
        self._queryset = self._queryset.filter(donor_id=self._params.donor)

    def _filter_by_search(self) -> None:
        query = SearchQuery(self._params.search, config="russian")
        self._queryset = self._queryset.filter(search_vector=query)

    def sort(self) -> None:
        if self._params.sort_by:
            if self._params.sort_by.removeprefix("-") == ProductSortBy.DISCOUNT:
                self._queryset = self._queryset.annotate(
                    discount=ExpressionWrapper(
                        F("price") / F("promo_price"), output_field=FloatField()
                    )
                )
            self._queryset = self._queryset.order_by(self._params.sort_by)
        else:
            self._queryset = self._queryset.order_by("id")
