import requests

from magnit_api.settings import BASE_URL


def get_raw_locations(session: requests.Session) -> requests.Response:
    response = session.get(
        BASE_URL + "/local/components/agima/choose.location/locations.js",
    )
    return response
