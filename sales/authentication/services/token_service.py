from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken

from authentication.types import JwtAuth


class TokenService:
    @staticmethod
    def create_tokens(user) -> JwtAuth:
        refresh_token = RefreshToken.for_user(user=user)
        access_token = refresh_token.access_token
        return JwtAuth(str(refresh_token), str(access_token))
    
    @staticmethod
    def blacklist_token(refresh_token: str) -> None:
        refresh = RefreshToken(refresh_token)
        refresh.blacklist()

    @staticmethod
    def blacklist_all_user_tokens(user_pk: int) -> None:
        for token in OutstandingToken.objects.filter(user_id=user_pk):
            BlacklistedToken.objects.get_or_create(token=token)
