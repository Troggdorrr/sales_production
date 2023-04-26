from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin

from products.services.CRUD import PromoTypeCRUD
from products.serializers import PromoTypeSerializer


class PromoTypeViewSet(GenericViewSet, RetrieveModelMixin, ListModelMixin):
    serializer_class = PromoTypeSerializer

    def get_queryset(self):
        return PromoTypeCRUD.get_list()
