from django.http import Http404
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.db.models import QuerySet

from products.models import Like, Product
from products.errors import ArleadyLiked


User = get_user_model()


class LikeCRUD:
    @staticmethod
    def get_list_by_user(user: User) -> QuerySet:
        return Like.objects.filter(user=user).select_related(
            "product",
            "product__donor",
            "product__promo",
            "product__promo__type",
        ).order_by("-id")

    @classmethod
    def create(cls, user: User, product_pk: int) -> Like:
        if cls.is_exists(user, product_pk):
            raise ArleadyLiked

        like = Like.objects.create(user=user, product_id=product_pk)
        return like

    @classmethod
    def is_exists(cls, user: User, product_pk: int) -> bool:
        try:
            cls.get(user=user, product_pk=product_pk)
            return True
        except Http404:
            return False

    @staticmethod
    def get(user: User, product_pk: int):
        return get_object_or_404(Like, user=user, product_id=product_pk)
