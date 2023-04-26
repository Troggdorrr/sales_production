from requests.cookies import create_cookie
from fake_useragent import FakeUserAgent

from magnit_api.settings import DOMAIN


class RequestUtils:
    @staticmethod
    def get_headers() -> dict:
        generator = FakeUserAgent()
        return {
            "User-Agent": generator["chrome"]
        }
    
    @staticmethod
    def get_geo_cookie(location_id: int) -> dict:
        return create_cookie("mg_geo_id", str(location_id), domain=DOMAIN)