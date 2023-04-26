from products.models import Shop


class ShopCRUD:
    @staticmethod
    def get_list_by_product(product_pk: int):
        return Shop.objects.filter(product__id=product_pk).select_related("city")