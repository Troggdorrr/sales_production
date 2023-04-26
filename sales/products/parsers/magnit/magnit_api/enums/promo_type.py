from enum import StrEnum


class PromoType(StrEnum):
    ONE_PLUS_ONE = "1_1"
    TWO_PLUS_ONE = "2_1"
    THREE_PLUS_ONE = "3_1"
    DISCOUNT = "skidka"
    PENSIONER_DISCOUNT = "skidka_p"
    CAREGORY_DISCOUNT = "skidka_kat"