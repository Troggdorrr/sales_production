from authentication.types import LogOutData

from .token_service import TokenService


class LogOutService:
    @staticmethod
    def logout(data: LogOutData) -> None:
        TokenService.blacklist_token(data.refresh)