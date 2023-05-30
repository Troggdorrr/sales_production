import logging

from products.models import Shop, City, Product, Promo, PromoType
from products.parsers import BaseParser

from .magnit_api import Client
from .magnit_api.types import (
    Shop as ApiShop,
    Product as ApiProduct,
    Promo as ApiPromo,
    City as ApiCity,
)


class MagnitParser(BaseParser):
    donor_name = "Магнит"
    donor_url = "https://magnit.ru/"
    donor_logo = "products/parsers/magnit/logo.svg"

    def save_data(self) -> None:
        client = Client()
        for city in client.get_cities():
            city_object = self._save_city(city)
            print(city_object)
            for shop in client.get_shops(city):
                shop_object = self._save_shop(shop, city_object)
                print(shop_object)
                for product in client.get_products(shop):
                    if product.price and product.promo_price:
                        print(self._save_product(product, shop_object))

    def _save_city(self, city: ApiCity) -> City:
        city_object, is_created = City.objects.get_or_create(
            name=city.name
        )
        return city_object
    
    def _save_shop(self, shop: ApiShop, city: City) -> Shop:
        shop_object, is_created = Shop.objects.get_or_create(
            address=shop.address,
            defaults={
                "city": city,
            },
        )
        return shop_object

    def _save_product(self, product: ApiProduct, shop: Shop) -> Product:
        product_object, is_created = Product.objects.update_or_create(
            url=product.href,
            donor=self.donor,
            defaults={
                "title": product.name,
                "poster": product.poster,
                "price": product.price,
                "promo_price": product.promo_price,
                "promo": self._save_promo(product.promo),
            },
        )
        product_object.shops.add(shop)
        return product_object

    def _save_promo(self, promo: ApiPromo) -> Promo:
        promo_objects, is_created = Promo.objects.get_or_create(
            date_begin=promo.date_begin,
            date_end=promo.date_end,
            type=self._save_promo_type(),
        )
        return promo_objects

    def _save_promo_type(self) -> PromoType:
        promo_type_object, is_created = PromoType.objects.get_or_create(name="Скидка")
        return promo_type_object

