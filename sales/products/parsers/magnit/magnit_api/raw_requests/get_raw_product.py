import requests

from magnit_api.settings import BASE_URL


def get_raw_product(session: requests.Session, id: int) -> requests.Response:
    response = session.get(
        BASE_URL + f"/promo/{id}/",
        allow_redirects=False,
    )
    return response
