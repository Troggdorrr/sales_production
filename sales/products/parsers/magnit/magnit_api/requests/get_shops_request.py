import requests
from requests import Response

from magnit_api.utils import HeadersGenerator
from magnit_api.types import City
from magnit_api.settings import BASE_API_URL


class GetShopsRequest:
    def __init__(self, city: City) -> None:
        self.city = city

    def get_shops(self) -> Response:
        return requests.get(
            BASE_API_URL + "/stores",
            headers=HeadersGenerator.get_api_headers(),
            params={"limit": 9999999, "City": self.city.name},
        )
