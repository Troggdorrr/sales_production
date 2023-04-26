from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

from users.services import UserCRUD

from authentication.models import ResetPaswordRequest
from authentication.types import ResetPasswordData
from authentication.errors import IdentifierDoesNotExists

from authentication.tasks import send_reset_password_email


User = get_user_model()


class ResetPasswordService:
    def __init__(self, data: ResetPasswordData) -> None:
        self._data = data
    
    def reset(self) -> None:
        user = self._find_user()
        request = self._create_reset_password_request(user)
        self._do_tasks(request)
    
    def _find_user(self) -> User:
        try:
            return UserCRUD.find_by_username_or_email(self._data.identifier)
        except ObjectDoesNotExist:
            raise IdentifierDoesNotExists
        
    def _create_reset_password_request(self, user: User) -> ResetPaswordRequest:
        return ResetPaswordRequest.objects.create(user=user)
    
    def _do_tasks(self, request: ResetPaswordRequest) -> None:
        send_reset_password_email.delay(request.user.email, request.uuid)
