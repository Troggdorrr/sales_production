import requests

from magnit_api.settings import BASE_URL
from magnit_api.enums import PromoType


def get_raw_product_links(
    session: requests.Session,
    page: int,
    promo_types: list[PromoType] = None,
) -> requests.Response:
    response = session.post(
        BASE_URL + "/promo/",
        data={"page": page},
        params={"type[]": promo_types},
    )
    return response
