from rest_framework.exceptions import APIException
from rest_framework import status


class IdentifierDoesNotExists(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = {
        "identifier": ["Пользователя с таким логином или почтой не существует"]
    }
    default_code = "identifier_does_not_exists"