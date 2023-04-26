from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin

from core.paginations import BigPagination

from products.services.CRUD import CityCRUD
from products.serializers import CitySerializer
from products.filters import CityFilterBackend


class CityViewSet(GenericViewSet, RetrieveModelMixin, ListModelMixin):
    pagination_class = BigPagination
    serializer_class = CitySerializer
    filter_backends = [CityFilterBackend]

    def get_queryset(self):
        return CityCRUD.get_list()