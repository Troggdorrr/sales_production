from datetime import datetime


class DateParser:
    @staticmethod
    def parse_date(raw_date: str) -> datetime:
        raw_date = raw_date.split("-")
        year = int(raw_date[0])
        month = int(raw_date[1])
        day = int(raw_date[2])
        return datetime(year, month, day)