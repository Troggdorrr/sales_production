from magnit_api.utils import DateParser

from magnit_api.types import Product, Promo
from magnit_api.settings import BASE_URL


class ProductParser:
    def __init__(self, raw_products: dict) -> None:
        self.raw_products = raw_products
    
    def get_products(self) -> list[Product]:
        products = []

        for raw_product in self.raw_products:
            try:
                products.append(self._get_product(raw_product))
            except:
                pass

        return products
    
    def _get_product(self, raw_product: dict) -> Product:
        return Product(
            id=raw_product["id"],
            href=self.__get_href(raw_product["productCode"]),
            name=raw_product["name"],
            poster=raw_product["image"],
            price=self.__normalize_price(raw_product.get("oldPrice")),
            promo_price=self.__normalize_price(raw_product.get("price")),
            promo=self.__get_promo(raw_product)
        )

    def __get_href(self, product_code: str) -> str:
        return BASE_URL + "/promo/" + product_code
    
    def __normalize_price(self, raw_price: int) -> float:
        if raw_price:
            return raw_price / 100
    
    def __get_promo(self, raw_product: dict) -> Promo:
        return Promo(
            date_begin=DateParser.parse_date(raw_product["startDate"]),
            date_end=DateParser.parse_date(raw_product["endDate"]),
        )
