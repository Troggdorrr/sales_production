from pyaterochka_api.types import Product, Promo
from pyaterochka_api.settings import BASE_URL

from .promo_parser import PromoParser


class ProductParser:
    def __init__(self, raw_product: dict):
        self._raw_product = raw_product

    def get_product(self) -> Product:
        id = self._get_id()
        return Product(
            id=id,
            href=self._get_href(id),
            name=self._get_name(),
            poster=self._get_poster(),
            price=self._get_price(),
            promo_price=self._get_promo_price(),
            promo=self._get_promo()
        )

    def _get_id(self) -> int:
        return self._raw_product["id"]
    
    def _get_href(self, id: int) -> str:
        return BASE_URL + f"/special_offers/{id}"
    
    def _get_name(self) -> str:
        return self._raw_product["name"]
    
    def _get_poster(self) -> str:
        return self._raw_product["img_link"]
    
    def _get_price(self) -> float:
        return float(self._raw_product["current_prices"]["price_reg__min"])
    
    def _get_promo_price(self) -> float:
        return float(self._raw_product["current_prices"]["price_promo__min"])
    
    def _get_promo(self) -> Promo:
        parser = PromoParser(self._raw_product["promo"])
        return parser.get_promo()
