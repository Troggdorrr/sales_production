from dataclasses import dataclass


@dataclass(frozen=True)
class ProductLink:
    id: int
    href: str