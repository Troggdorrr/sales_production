from django.db.models import QuerySet
from django.http import HttpRequest

from rest_framework import filters


class ConstructorFilterBackend(filters.BaseFilterBackend):
    filter_service = None

    def filter_queryset(self, request: HttpRequest, queryset: QuerySet, view) -> QuerySet:
        params = self.get_params(request)
        params.validate()

        service_queryset = self.filter_service(queryset=queryset, params=params)
        service_queryset.filter()
        service_queryset.sort()

        return service_queryset.queryset
    
    def get_params(self, request: HttpRequest):
        pass