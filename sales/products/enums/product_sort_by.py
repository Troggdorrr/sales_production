from .sort_by_enum import SortByEnum


class ProductSortBy(SortByEnum):
    ID: str = "id"
    PRICE: str = "price"
    PROMO_PRICE: str = "promo_price"
    DISCOUNT: str = "discount"