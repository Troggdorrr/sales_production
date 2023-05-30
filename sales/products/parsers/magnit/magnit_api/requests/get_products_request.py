import requests
from requests import Response

from magnit_api.utils import HeadersGenerator
from magnit_api.types import Shop
from magnit_api.settings import BASE_API_URL


class GetProductsRequest:
    def __init__(self, shop: Shop) -> None:
        self.shop = shop

    def get_products(self) -> Response:
        return requests.get(
            BASE_API_URL + "/promotions",
            headers=HeadersGenerator.get_api_headers(),
            params={
                "limit": 9999999,
                "storeId": self.shop.id,
                "adult": "true",
            },
        )
