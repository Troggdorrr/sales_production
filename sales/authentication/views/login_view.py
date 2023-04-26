from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import HttpRequest

from authentication.services import LoginService
from authentication.types import JwtAuth, LogInData


class LogInView(APIView):
    def post(self, request: HttpRequest) -> Response:
        data = self._create_data()
        tokens = self._create_user(data)
        return Response(tokens.data)

    def _create_data(self) -> None:
        data = LogInData(
            email=self.request.POST.get("email"),
            password=self.request.POST.get("password"),
        )
        data.validate()
        return data

    def _create_user(self, data: LogInData) -> JwtAuth:
        service = LoginService(data)
        tokens = service.login()
        return tokens
