from magnit_api.types import Shop


class ShopParser:
    def __init__(self, raw_shops: dict) -> None:
        self.raw_shops = raw_shops

    def get_shops(self) -> list[Shop]:
        shops = []

        for raw_shop in self.raw_shops:
            shops.append(self._get_shop(raw_shop))

        return shops

    def _get_shop(self, raw_shop: dict) -> Shop:
        return Shop(
            id=raw_shop["id"],
            address=raw_shop["address"],
        )
