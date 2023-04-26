from functools import lru_cache
import json

from magnit_api.types import Store


class StoreParser:
    def __init__(self, raw_promo_data: str) -> None:
        self._promo_data = json.loads(raw_promo_data)

    def parse(self) -> list[Store]:
        stores = []

        for raw_store in self._promo_data["points"]:
            store = self._parse_store(raw_store)
            stores.append(store)

        return stores

    def _parse_store(self, raw_store: dict) -> Store:
        return Store(
            address=self._parse_address(raw_store),
        )
    
    def _parse_address(self, raw_store: dict) -> str:
        return raw_store["address"]