from rest_framework.exceptions import APIException
from rest_framework import status


class ResetUUIDDoesNotExists(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = {
        "uuid": ["Заданный uuid для восстановления пароля не найден"]
    }
    default_code = "reset_uuid_does_not_exists"