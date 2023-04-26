from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import HttpRequest

from authentication.services import SignUpService
from authentication.types import JwtAuth, SignUpData


class SignUpView(APIView):
    def post(self, request: HttpRequest) -> Response:
        data = self._create_data()
        tokens = self._create_user(data)
        return Response(tokens.data, status=201)

    def _create_data(self) -> None:
        data = SignUpData(
            email=self.request.POST.get("email"),
            password=self.request.POST.get("password"),
            username=self.request.POST.get("username"),
        )
        data.validate()
        return data

    def _create_user(self, data: SignUpData) -> JwtAuth:
        service = SignUpService(data)
        tokens = service.signup()
        return tokens
