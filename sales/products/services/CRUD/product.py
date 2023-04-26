from django.db.models import QuerySet, Exists, OuterRef
from django.contrib.postgres.search import TrigramDistance
from products.models import Product, Like


class ProductCRUD:
    @classmethod
    def get_auth_similiar_products(cls, product: Product, user):
        similiar_products = cls._add_similarity_logic(cls.get_auth_list(user), product)
        return similiar_products

    @classmethod
    def get_similiar_products(cls, product: Product) -> QuerySet:
        similiar_products = cls._add_similarity_logic(cls.get_list(), product)
        return similiar_products

    @classmethod
    def _add_similarity_logic(cls, queryset: QuerySet, product: Product) -> QuerySet:
        queryset = queryset.annotate(
            similarity=TrigramDistance("title", product.title)
        ).exclude(pk=product.pk)
        return queryset

    @classmethod
    def get_auth_list(cls, user) -> QuerySet:
        default_list = cls.get_list()
        auth_list = cls._annotate_is_liked(default_list, user)
        return auth_list

    @staticmethod
    def get_list() -> QuerySet:
        return Product.objects.select_related(
            "promo", "promo__type", "donor"
        )

    @staticmethod
    def _annotate_is_liked(queryset: QuerySet, user) -> QuerySet:
        return queryset.prefetch_related("likes").annotate(
            is_liked=Exists(Like.objects.filter(product=OuterRef("pk"), user=user))
        )

    @classmethod
    def is_exists(cls, pk: int) -> bool:
        return cls.get(pk=pk) is not None

    @staticmethod
    def get(pk: int) -> Product | None:
        try:
            product = Product.objects.get(pk=pk)
            return product
        except (Product.DoesNotExist, ValueError):
            return None
