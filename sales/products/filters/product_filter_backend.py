from django.http import HttpRequest

from products.types import ProductFilterParams
from products.services.filters import ProductFilter

from .constructor_filter_backend import ConstructorFilterBackend


class ProductFilterBackend(ConstructorFilterBackend):
    filter_service = ProductFilter
    
    def get_params(self, request: HttpRequest):
        return ProductFilterParams(
            price__lt=request.GET.get("price__lt"),
            price__gt=request.GET.get("price__gt"),
            is_expired=request.GET.get("is_expired"),
            promo_type=request.GET.get("promo_type"),
            city=request.GET.get("city"),
            donor=request.GET.get("donor"),
            sort_by=request.GET.get("sort_by"),
            search=request.GET.get("search")
        )