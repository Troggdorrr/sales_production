from enum import StrEnum


class SortByEnum(StrEnum):
    @classmethod
    def has(cls, value: str) -> bool:
        return value.removeprefix("-") in cls._value2member_map_.keys()