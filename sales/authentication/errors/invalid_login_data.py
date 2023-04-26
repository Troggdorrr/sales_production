from rest_framework.exceptions import APIException
from rest_framework import status


class InvalidLoginData(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = "Неправильный логин или пароль"
    default_code = "invalid_login_data"