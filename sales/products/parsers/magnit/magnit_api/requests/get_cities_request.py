import requests
from requests import Response

from magnit_api.utils import HeadersGenerator
from magnit_api.settings import BASE_API_URL


class GetCitiesRequest:
    def get_cities(self) -> Response:
        return requests.get(
            BASE_API_URL + "/cities",
            headers=HeadersGenerator.get_api_headers(),
            params={"limit": 9999999},
        )
