from dataclasses import dataclass

from .promo import Promo
from .store import Store


@dataclass(frozen=True)
class Product:
    id: int
    href: str
    name: str
    poster: str
    price: float
    promo_price: float
    promo: Promo
    stores: list[Store]