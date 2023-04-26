from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Promo:
    date_begin: date
    date_end: date
    type: str
