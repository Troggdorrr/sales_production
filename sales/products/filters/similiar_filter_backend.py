from django.http import HttpRequest

from products.types import SimiliarFilterParams
from products.services.filters import SimiliarFilter

from .constructor_filter_backend import ConstructorFilterBackend


class SimiliarFilterBackend(ConstructorFilterBackend):
    filter_service = SimiliarFilter
    
    def get_params(self, request: HttpRequest):
        return SimiliarFilterParams(
            city=request.GET.get("city"),
            is_expired=request.GET.get("is_expired"),
        )