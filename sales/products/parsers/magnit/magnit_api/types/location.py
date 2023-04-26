from dataclasses import dataclass


@dataclass(frozen=True)
class Location:
    id: int
    name: str