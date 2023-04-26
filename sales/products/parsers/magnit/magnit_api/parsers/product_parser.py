from bs4 import BeautifulSoup, Tag

from functools import lru_cache
import re

from magnit_api.utils import ProductHrefNormalizer
from magnit_api.types import Product, Promo, Store
from magnit_api.settings import BASE_URL

from .promo_parser import PromoParser
from .store_parser import StoreParser


class ProductParser:
    def __init__(self, raw_product: str):
        self._markup = raw_product
        self._parser = BeautifulSoup(self._markup, "lxml")

    def parse(self) -> Product:
        return Product(
            id=self._parse_id(),
            href=self._parse_href(),
            name=self._parse_name(),
            poster=self._parse_poster(),
            price=self._parse_price(),
            promo_price=self._parse_promo_price(),
            promo=self._parse_promo(),
            stores=self._parse_stores(),
        )

    def _parse_id(self) -> int:
        normalizer = self.__get_normalizer()
        return normalizer.get_id()

    def _parse_href(self) -> str:
        normalizer = self.__get_normalizer()
        return normalizer.get_href()

    @lru_cache
    def __get_normalizer(self) -> ProductHrefNormalizer:
        tag = self.__get_href_tag()
        return ProductHrefNormalizer(tag["content"])

    def __get_href_tag(self) -> Tag:
        return self._parser.find("meta", {"property": "og:url"})

    def _parse_name(self) -> str:
        return self._parser.find("div", {"class": "action__title"}).get_text(strip=True)

    def _parse_poster(self) -> str | None:
        tag = self._parser.find("img", {"class": "action__image"})
        if not tag:
            return None
        return BASE_URL + tag["data-src"]

    def _parse_price(self) -> float | None:
        tag = self._parser.find("div", {"class": "label__price_old"})
        if not tag:
            return None
        return self.__parse_price_label(tag)

    def _parse_promo_price(self) -> float | None:
        tag = self._parser.find("div", {"class": "label__price_new"})
        if not tag:
            return None
        return self.__parse_price_label(tag)

    def __parse_price_label(self, tag: Tag) -> float:
        integer_part = tag.find("span", {"class": "label__price-integer"}).get_text(
            strip=True
        )
        decimal_part = tag.find("span", {"class": "label__price-decimal"}).get_text(
            strip=True
        )
        price = f"{integer_part}.{decimal_part}"
        return float(price)

    def _parse_promo(self) -> Promo:
        raw_promo = self._parser.find("div", {"class": "action__header"})
        parser = PromoParser(raw_promo)
        return parser.parse()

    def _parse_stores(self) -> list[Store]:
        raw_promo_data = self.__parse_promo_data()
        parser = StoreParser(raw_promo_data)
        return parser.parse()

    def __parse_promo_data(self) -> str:
        return re.search(r"var promoData = (.*?);", self._markup).group(1)
