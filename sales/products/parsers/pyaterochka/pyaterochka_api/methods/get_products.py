from pyaterochka_api.raw_methods import get_products
from pyaterochka_api.parsers import ProductParser

from pyaterochka_api.types import Product


class GetProducts:
    def get_products(self, page: int = 1, per_page: int = 20, store: str = None):
        raw_products = self._get_raw_products(page, per_page, store)
        products = self._parse_products(raw_products)
        return products

    def _get_raw_products(self, page: int = 1, per_page: int = 20, store: str = None) -> list[dict]:
        response = get_products(page=page, per_page=per_page, store=store)
        return response.json()["results"]

    def _parse_products(self, raw_products: list[dict]) -> list[Product]:
        products = []

        for raw_product in raw_products:
            products.append(self._parse_product(raw_product))

        return products

    def _parse_product(self, raw_product: dict) -> Product:
        parser = ProductParser(raw_product)
        return parser.get_product()
