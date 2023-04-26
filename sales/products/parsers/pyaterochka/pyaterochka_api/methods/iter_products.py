from .get_products import GetProducts
from pyaterochka_api.types import Product


class IterProducts:
    def iter_products(self, store: str = None):
        page = 1

        while True:
            chuck = self.__get_chuck(page, store)

            if not chuck:
                break

            for product in chuck:
                yield product

            page += 1

    def __get_chuck(self, page, store: str = None) -> list[Product]:
        return GetProducts().get_products(page, store=store)
