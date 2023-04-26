from django.core.paginator import Paginator
from django.utils.functional import cached_property

from rest_framework.pagination import PageNumberPagination


class FasterDjangoPaginator(Paginator):
    @cached_property
    def count(self):
        return self.object_list.values('id').count()


class DefaultPagination(PageNumberPagination):
    django_paginator_class = FasterDjangoPaginator
    page_size = 30
    max_page_size = 50
    page_size_query_param = "per_page"
    page_query_param = "page"