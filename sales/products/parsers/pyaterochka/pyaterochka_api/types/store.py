from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Store:
    city_name: str
    code: str
    address: str