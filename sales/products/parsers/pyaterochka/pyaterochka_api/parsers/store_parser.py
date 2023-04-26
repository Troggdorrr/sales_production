from datetime import date

from pyaterochka_api.types import Store


class StoreParser:
    def __init__(self, raw_store: dict):
        self._raw_store = raw_store

    def get_store(self) -> Store:
        return Store(
            city_name=self._get_city_name(),
            code=self._get_code(),
            address=self._get_address()
        )

    def _get_city_name(self) -> date:
        return self._raw_store["city_name"]
    
    def _get_code(self) -> date:
        return self._raw_store["sap_code"]

    def _get_address(self) -> date:
        return self._raw_store["address"]