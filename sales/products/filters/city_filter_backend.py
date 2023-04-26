from django.http import HttpRequest

from products.types import CityFilterParams
from products.services.filters import CityFilter

from .constructor_filter_backend import ConstructorFilterBackend


class CityFilterBackend(ConstructorFilterBackend):
    filter_service = CityFilter

    def get_params(self, request: HttpRequest):
        return CityFilterParams(
            sort_by=request.GET.get("sort_by"), search=request.GET.get("search")
        )
