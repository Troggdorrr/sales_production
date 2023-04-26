from django.http import HttpRequest

from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnProfile(BasePermission):
    def has_permission(self, request: HttpRequest, view) -> bool:
        user_pk = view.kwargs.get("user_pk") or view.kwargs.get("pk")
        if request.user.is_authenticated:
            if user_pk:
                return user_pk == str(request.user.id)
        return False
