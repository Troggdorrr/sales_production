from .default_pagination import DefaultPagination


class BigPagination(DefaultPagination):
    page_size = 50
    max_page_size = 100