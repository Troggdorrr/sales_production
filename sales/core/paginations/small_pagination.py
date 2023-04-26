from .default_pagination import DefaultPagination


class SmallPagination(DefaultPagination):
    page_size = 10
    max_page_size = 20