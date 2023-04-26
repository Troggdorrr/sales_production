from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from core.paginations import SmallPagination

from products.services.CRUD import LikeCRUD
from products.serializers import LikeSerializer

from users.permissions import IsOwnProfile


class UserLikesViewSet(GenericViewSet, ListModelMixin):
    serializer_class = LikeSerializer
    permission_classes = [IsOwnProfile]
    pagination_class = SmallPagination

    def get_queryset(self):
        return LikeCRUD.get_list_by_user(self.request.user)