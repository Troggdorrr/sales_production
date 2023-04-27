import logging

from products.models import Shop, City, Product, Promo, PromoType
from products.parsers import BaseParser

from .magnit_api import Client
from .magnit_api.enums import PromoType as ApiPromoType
from .magnit_api.types import (
    Store as ApiStore,
    Product as ApiProduct,
    Promo as ApiPromo,
)
from .magnit_api.errors import ProductDoesNotExists


class MagnitParser(BaseParser):
    donor_name = "Магнит"
    donor_url = "https://magnit.ru/"
    donor_logo = "products/parsers/magnit/logo.svg"

    def save_data(self) -> None:
        client = Client()
        for location in client.get_locations():
            client.set_location(location.id)
            city_object = self._save_city(location.name)
            self._save_products(client, city_object)

    def _save_city(self, city: str) -> City:
        city_object, is_created = City.objects.get_or_create(
            name=self.__normalize_city(city)
        )
        return city_object

    def __normalize_city(self, city: str) -> str:
        return city.replace(". ", ".")

    def _save_products(self, client: Client, city: City) -> None:
        promo_types = [
            ApiPromoType.DISCOUNT,
            ApiPromoType.ONE_PLUS_ONE,
            ApiPromoType.TWO_PLUS_ONE,
            ApiPromoType.THREE_PLUS_ONE,
        ]
        for product_link in client.iter_product_links(promo_types):
            try:
                product = client.get_product(product_link.id)
                if not product.price or not product.promo_price:
                    continue
            except ProductDoesNotExists:
                continue
            except Exception as e:
                logging.exception("Error in magnit parser")
                continue

            self._save_product_with_shops(product, city)

    def _save_product_with_shops(self, product: ApiProduct, city: City):
        product_object = self._save_product(product)
        shop_objects = self._save_shops(product.stores, city)
        self._add_shops(product_object, shop_objects)

    def _save_product(self, product: ApiProduct) -> Product:
        product_object, is_created = Product.objects.update_or_create(
            title=product.name,
            url=product.href,
            donor=self.donor,
            defaults={
                "poster": product.poster,
                "price": product.price,
                "promo_price": product.promo_price,
                "promo": self._save_promo(product.promo),
            },
        )
        return product_object

    def _save_promo(self, promo: ApiPromo) -> Promo:
        promo_objects, is_created = Promo.objects.get_or_create(
            date_begin=promo.date_begin,
            date_end=promo.date_end,
            type=self._save_promo_type(promo.type),
        )
        return promo_objects

    def _save_promo_type(self, promo_type: str) -> PromoType:
        promo_type_object, is_created = PromoType.objects.get_or_create(name=promo_type)
        return promo_type_object

    def _save_shops(self, stores: list[ApiStore], city: City) -> list[Shop]:
        shops = []

        for store in stores:
            shop_object = self._save_shop(store, city)
            shops.append(shop_object)

        return shops

    def _save_shop(self, store: ApiStore, city: City) -> Shop:
        shop_object, is_created = Shop.objects.get_or_create(
            address=store.address,
            defaults={
                "city": city,
            },
        )
        return shop_object

    def _add_shops(self, product: Product, shops: list[Shop]) -> None:
        product.shops.add(*shops)
