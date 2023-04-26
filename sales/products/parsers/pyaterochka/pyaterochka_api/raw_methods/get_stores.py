import requests
from requests import Response

from pyaterochka_api.settings import BASE_API_URL_V3


def get_stores(page: int = 1, per_page: int = 20) -> Response:
    url = BASE_API_URL_V3 + "/stores/"
    params = {
        "page": page,
        "records_per_page": per_page
    }
    response = requests.get(url, params=params)
    return response