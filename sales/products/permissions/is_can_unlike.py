from rest_framework.permissions import BasePermission


class IsCanUnlike(BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.method == "DELETE":
            return view.kwargs["pk"] == str(request.user.pk)
        else:
            return True