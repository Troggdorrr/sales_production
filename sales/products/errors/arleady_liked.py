from rest_framework.exceptions import APIException
from rest_framework import status


class ArleadyLiked(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "Товар уже в избранном"
    default_code = "arleady_liked"