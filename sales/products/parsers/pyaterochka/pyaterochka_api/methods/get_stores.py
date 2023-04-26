from pyaterochka_api.raw_methods import get_stores
from pyaterochka_api.parsers import StoreParser

from pyaterochka_api.types import Store


class GetStores:
    def get_stores(self, page: int = 1, per_page: int = 20):
        raw_stores = self._get_raw_stores(page, per_page)
        stores = self._parse_stores(raw_stores)
        return stores

    def _get_raw_stores(self, page: int = 1, per_page: int = 20) -> list[dict]:
        response = get_stores(page=page, per_page=per_page)
        return response.json()["results"]

    def _parse_stores(self, raw_stores: list[dict]) -> list[Store]:
        stores = []

        for raw_product in raw_stores:
            stores.append(self._parse_store(raw_product))

        return stores

    def _parse_store(self, raw_store: dict) -> Store:
        parser = StoreParser(raw_store)
        return parser.get_store()
