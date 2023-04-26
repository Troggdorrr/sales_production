from django.http import Http404

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from core.paginations import SmallPagination

from products.services.CRUD import ProductCRUD
from products.serializers import ProductSerializer, AuthProductSerializer
from products.filters import SimiliarFilterBackend


class SimiliarViewSet(GenericViewSet, ListModelMixin):
    pagination_class = SmallPagination
    filter_backends = [SimiliarFilterBackend]

    def list(self, request, *args, **kwargs):
        product = ProductCRUD.get(self.kwargs["product_pk"])
        if not product:
            raise Http404
        else:
            self.product = product
        return super().list(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return AuthProductSerializer
        else:
            return ProductSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return ProductCRUD.get_auth_similiar_products(self.product, self.request.user)
        else:
            return ProductCRUD.get_similiar_products(self.product)