from datetime import date

import re


class PromoDateConverter:
    months = {
        "января": 1,
        "февраля": 2,
        "марта": 3,
        "апреля": 4,
        "мая": 5,
        "июня": 6,
        "июля": 7,
        "августа": 8,
        "сентября": 9,
        "декабря": 12,
        "октября": 10,
        "ноября": 11,
    }

    def __init__(self, promo_date: str):
        self._promo_date = promo_date

    def get_date_begin(self) -> date:
        raw_date = re.search(r"с *?(\d{1,2} .*?) ", self._promo_date).group(1)
        return self._convert_raw_date(raw_date)

    def get_date_end(self) -> date:
        raw_date = re.search(r"по *?(\d{1,2} .*)", self._promo_date).group(1)
        return self._convert_raw_date(raw_date)

    def _convert_raw_date(self, raw_date: str) -> date:
        year = date.today().year
        month = self.months[raw_date.split(" ")[1]]
        day = int(raw_date.split(" ")[0])
        return date(year, month, day)
    

a = PromoDateConverter("с 12 апреля по 18 апреля")
a.get_date_begin()