from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class Shop:
    id: int
    address: str