from rest_framework.views import APIView
from rest_framework.response import Response

from django.http import HttpRequest

from authentication.services import LogOutService
from authentication.types import LogOutData


class LogOutView(APIView):
    def post(self, request: HttpRequest) -> Response:
        data = self._get_data()
        LogOutService.logout(data)
        return Response(status=204)

    def _get_data(self):
        data = LogOutData(
            refresh=self.request.POST.get("refresh")
        )
        data.validate()
        return data