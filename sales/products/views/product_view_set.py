from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin

from core.paginations import DefaultPagination

from products.services.CRUD import ProductCRUD
from products.serializers import ProductSerializer, AuthProductSerializer
from products.filters import ProductFilterBackend


class ProductViewSet(GenericViewSet, RetrieveModelMixin, ListModelMixin):
    pagination_class = DefaultPagination
    filter_backends = [ProductFilterBackend]

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            return AuthProductSerializer
        else:
            return ProductSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return ProductCRUD.get_auth_list(self.request.user)
        else:
            return ProductCRUD.get_list()