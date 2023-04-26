from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin

from products.services.CRUD import DonorCRUD
from products.serializers import DonorSerializer


class DonorViewSet(GenericViewSet, RetrieveModelMixin, ListModelMixin):
    serializer_class = DonorSerializer

    def get_queryset(self):
        return DonorCRUD.get_list()
