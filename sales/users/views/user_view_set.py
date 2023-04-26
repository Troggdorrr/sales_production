from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import RetrieveModelMixin

from users.services import UserCRUD
from users.serializers import UserSerializer
from users.permissions import IsOwnProfile


class UserViewSet(GenericViewSet, RetrieveModelMixin):
    serializer_class = UserSerializer
    permission_classes = [IsOwnProfile]

    def get_queryset(self):
        return UserCRUD.get_list()