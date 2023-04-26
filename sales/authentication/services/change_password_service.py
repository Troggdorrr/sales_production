from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.conf import settings

from authentication.models import ResetPaswordRequest
from authentication.types import ChangePasswordData
from authentication.errors import ResetUUIDDoesNotExists

from .token_service import TokenService


User = get_user_model()


class ChangePasswordService:
    def __init__(self, data: ChangePasswordData) -> None:
        self._data = data

    def change(self) -> None:
        reset_request = self._get_reset_request()
        self._change_password(reset_request.user)
        self._blacklist_all_tokens(reset_request.user)
        reset_request.is_used = True
        reset_request.save()

    def _get_reset_request(self) -> ResetPaswordRequest:
        try: 
            return ResetPaswordRequest.objects.get(
                uuid=self._data.uuid,
                is_used=False,
                created_at__gt=timezone.now()
                - settings.RESET_PASSWORD_REQUEST_LIFETIME,
            )
        except ObjectDoesNotExist:
            raise ResetUUIDDoesNotExists

    def _change_password(self, user: User) -> None:
        user.set_password(self._data.password)
        user.save()

    def _blacklist_all_tokens(self, user: User) -> None:
        TokenService.blacklist_all_user_tokens(user.pk)