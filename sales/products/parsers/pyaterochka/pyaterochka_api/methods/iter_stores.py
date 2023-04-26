from .get_stores import GetStores
from pyaterochka_api.types import Store


class IterStores:
    def iter_stores(self):
        page = 1

        while True:
            chuck = self.__get_chuck(page)

            if not chuck:
                break

            for store in chuck:
                yield store

            page += 1

    def __get_chuck(self, page) -> list[Store]:
        return GetStores().get_stores(page)
