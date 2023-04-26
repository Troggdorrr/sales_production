from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import HttpRequest

from authentication.services import ChangePasswordService
from authentication.types import ChangePasswordData


class ChangePasswordView(APIView):
    def post(self, request: HttpRequest) -> Response:
        data = self._create_data()
        self._change_password(data)
        return Response(status=204)

    def _create_data(self) -> None:
        data = ChangePasswordData(
            uuid=self.request.POST.get("uuid"),
            password=self.request.POST.get("password")
        )
        data.validate()
        return data

    def _change_password(self, data: ChangePasswordData) -> None:
        service = ChangePasswordService(data)
        service.change()
