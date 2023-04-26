from datetime import date

from pyaterochka_api.types import Promo


class PromoParser:
    def __init__(self, raw_promo: dict):
        self._raw_promo = raw_promo

    def get_promo(self) -> Promo:
        return Promo(
            date_begin=self._get_date_begin(),
            date_end=self._get_date_end(),
            type=self._get_type()
        )

    def _get_date_begin(self) -> date:
        raw_date = self._raw_promo["date_begin"]
        return self.__parse_date(raw_date)
    
    def _get_date_end(self) -> date:
        raw_date = self._raw_promo["date_end"]
        return self.__parse_date(raw_date)

    def __parse_date(self, raw_date: str) -> date:
        splited_date = raw_date.split("-")
        year = int(splited_date[0])
        month = int(splited_date[1])
        day = int(splited_date[2])
        return date(year, month, day)
    
    def _get_type(self) -> str:
        return self._raw_promo["type"]
