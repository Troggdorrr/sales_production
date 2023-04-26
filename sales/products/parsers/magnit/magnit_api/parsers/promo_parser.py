from bs4 import Tag

from datetime import date
from functools import lru_cache

from magnit_api.utils import PromoDateConverter
from magnit_api.types import Promo


class PromoParser:
    def __init__(self, promo_tag: Tag):
        self._parser = promo_tag

    def parse(self) -> Promo:
        return Promo(
            date_begin=self._parse_date_begin(),
            date_end=self._parse_date_end(),
            type=self._parse_type(),
        )

    def _parse_date_begin(self) -> date:
        converter = self.__get_converter()
        return converter.get_date_begin()

    def _parse_date_end(self) -> date:
        converter = self.__get_converter()
        return converter.get_date_end()

    @lru_cache
    def __get_converter(self) -> PromoDateConverter:
        raw_date = self.__get_raw_date()
        return PromoDateConverter(raw_date)

    def __get_raw_date(self) -> str:
        return self._parser.find("div", {"class": "action__date-label"}).get_text(
            strip=True
        )
    
    def _parse_type(self) -> str:
        return self._parser.find("p", {"class": "action__name-text"}).get_text(strip=True)
