from django.http import HttpRequest

from products.types import ShopFilterParams
from products.services.filters import ShopFilter

from .constructor_filter_backend import ConstructorFilterBackend


class ShopFilterBackend(ConstructorFilterBackend):
    filter_service = ShopFilter

    def get_params(self, request: HttpRequest):
        return ShopFilterParams(city=request.GET.get("city"))