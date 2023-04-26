from django.http import Http404

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin

from core.paginations import DefaultPagination

from products.services.CRUD import ShopCRUD, ProductCRUD
from products.serializers import ShopSerializer
from products.filters import ShopFilterBackend


class ShopViewSet(GenericViewSet, RetrieveModelMixin, ListModelMixin):
    serializer_class = ShopSerializer
    pagination_class = DefaultPagination
    filter_backends = [ShopFilterBackend]

    def list(self, request, *args, **kwargs):
        if not ProductCRUD.is_exists(self.kwargs["product_pk"]):
            raise Http404
        return super().list(request, *args, **kwargs)

    def get_queryset(self):
        return ShopCRUD.get_list_by_product(self.kwargs["product_pk"])
