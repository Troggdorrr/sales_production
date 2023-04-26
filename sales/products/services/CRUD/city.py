from products.models import City


class CityCRUD:
    @staticmethod
    def get_list():
        return City.objects.all()

    @staticmethod
    def get_product_cities(product_pk: int):
        return City.objects.filter(shops__product__id=product_pk)