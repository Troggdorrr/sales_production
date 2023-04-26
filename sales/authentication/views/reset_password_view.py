from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import HttpRequest

from authentication.services import ResetPasswordService
from authentication.types import ResetPasswordData


class ResetPasswordView(APIView):
    def post(self, request: HttpRequest) -> Response:
        data = self._create_data()
        self._reset_password(data)
        return Response(status=204)

    def _create_data(self) -> None:
        data = ResetPasswordData(
            identifier=self.request.POST.get("identifier"),
        )
        data.validate()
        return data

    def _reset_password(self, data: ResetPasswordData) -> None:
        service = ResetPasswordService(data)
        service.reset()
