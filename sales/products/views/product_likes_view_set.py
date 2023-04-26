from django.http import Http404

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin

from products.services.CRUD import LikeCRUD, ProductCRUD
from products.serializers import LikeSerializer
from products.permissions import IsCanUnlike


class ProductLikesViewSet(GenericViewSet, CreateModelMixin, DestroyModelMixin):
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated, IsCanUnlike]

    def create(self, request, *args, **kwargs):
        if not ProductCRUD.is_exists(self.kwargs.get("product_pk")):
            raise Http404
        return super().create(request, *args, **kwargs)

    def get_object(self):
        return LikeCRUD.get(self.request.user, product_pk=self.kwargs.get("product_pk"))