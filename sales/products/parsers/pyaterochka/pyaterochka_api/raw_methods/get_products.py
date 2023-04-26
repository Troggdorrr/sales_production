import requests
from requests import Response

from pyaterochka_api.settings import BASE_API_URL_V2


def get_products(page: int = 1, per_page: int = 20, store: str = None) -> Response:
    url = BASE_API_URL_V2 + "/special_offers/"
    params = {
        "page": page,
        "records_per_page": per_page,
        "store": store
    }
    response = requests.get(url, params=params)
    return response