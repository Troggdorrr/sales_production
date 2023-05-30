from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class City:
    id: str
    name: str