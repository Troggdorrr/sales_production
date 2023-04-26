from django.contrib.auth import get_user_model
from django.db.models import QuerySet, Q


User = get_user_model()


class UserCRUD:
    @staticmethod
    def get_list() -> QuerySet:
        return User.objects.all()

    @staticmethod
    def get_by_email(email: str) -> User:
        return User.objects.get(email__iexact=email)
    
    @staticmethod
    def get_by_username(username: str) -> User:
        return User.objects.get(username__iexact=username)
    
    @staticmethod
    def find_by_username_or_email(identifier: str) -> User:
        return User.objects.get(Q(username__iexact=identifier) | Q(email__iexact=identifier))