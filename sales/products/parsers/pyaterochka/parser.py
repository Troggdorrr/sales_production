from products.models import Shop, City, Product, Promo, PromoType
from products.parsers import BaseParser

from .pyaterochka_api import Client
from .pyaterochka_api.types import Store as ApiStore, Product as ApiProduct, Promo as ApiPromo


class PyaterochkaParser(BaseParser):
    donor_name = "Пятёрочка"
    donor_url = "https://5ka.ru/"
    donor_logo = "products/parsers/pyaterochka/logo.svg"

    def save_data(self) -> None:
        api_client = Client()
        for store in api_client.iter_stores():
            shop = self._save_shop(store)
            for product in api_client.iter_products(store=store.code):
                self._save_product(product, shop)

    def _save_shop(self, store: ApiStore) -> Shop:
        shop_object, is_created = Shop.objects.get_or_create(
            address=store.address,
            defaults={
                "city": self._save_city(store.city_name),
            },
        )
        return shop_object

    def _save_city(self, city: str) -> City:
        city_object, is_created = City.objects.get_or_create(
            name=city
        )
        return city_object

    def _save_product(self, product: ApiProduct, shop: Shop):
        product_object, is_created = Product.objects.update_or_create(
            title=product.name,
            url=product.href,
            donor=self.donor,
            defaults={
                "poster": product.poster,
                "price": product.price,
                "promo_price": product.promo_price,
                "promo": self._save_promo(product.promo)
            }
        )
        product_object.shops.add(shop)
        return product_object

    def _save_promo(self, promo: ApiPromo) -> Promo:
        promo_objects, is_created = Promo.objects.get_or_create(
            date_begin=promo.date_begin,
            date_end=promo.date_end,
            type=self._save_promo_type(promo.type)
        )
        return promo_objects

    def _save_promo_type(self, promo_type: str):
        promo_type_object, is_created = PromoType.objects.get_or_create(
            name=self.__normalize_promo_type(promo_type)
        )
        return promo_type_object
    
    def __normalize_promo_type(self, promo_type: str):
        if not promo_type:
            return "Скидка"
        return promo_type
