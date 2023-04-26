from requests import Session

from typing import Generator

from .raw_requests import get_raw_product_links, get_raw_product, get_raw_locations
from .parsers import ProductLinkParser, ProductParser, LocationParser
from .types import ProductLink, Product, Location
from .errors import ProductDoesNotExists
from .enums import PromoType
from .utils import RequestUtils


class Client:
    def __init__(self) -> None:
        self._session = self.__create_session()
    
    def __create_session(self) -> Session:
        session = Session()
        session.headers = RequestUtils.get_headers()
        return session

    def iter_product_links(self, promo_types: list[PromoType] = None) -> Generator[ProductLink, None, None]:
        page = 1

        while True:
            chunck = self.get_product_links(page, promo_types)

            if not chunck:
                break
            else:
                page += 1

            for link in chunck:
                yield link

    def get_product_links(self, page: int, promo_types: list[PromoType] = None) -> list[ProductLink]:
        response = get_raw_product_links(self._session, page, promo_types)
        parser = ProductLinkParser(response.text)
        return parser.parse()
    
    def get_product(self, id: int) -> Product:
        response = get_raw_product(self._session, id)

        if response.status_code == 302:
            raise ProductDoesNotExists(id)

        parser = ProductParser(response.text)
        return parser.parse()
    
    def get_locations(self) -> list[Location]:
        response = get_raw_locations(self._session)
        parser = LocationParser(response.text)
        return parser.parse()
    
    def set_location(self, location_id: int) -> None:
        self._session.cookies.set_cookie(RequestUtils.get_geo_cookie(location_id))