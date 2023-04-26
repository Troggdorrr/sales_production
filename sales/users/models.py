from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)

from products.models import Product


class UserAccountManager(BaseUserManager):
    use_in_migrations = True

    def create_user(self, email: str, password: str, username: str, **extra_fields):
        return self._create_user(email, password, username, **extra_fields)

    def create_superuser(
        self, email: str, password: str, username: str, **extra_fields
    ):
        extra_fields["is_staff"] = True
        extra_fields["is_superuser"] = True
        return self._create_user(email, password, username, **extra_fields)

    def _create_user(self, email: str, password: str, username: str, **extra_fields):
        self.__validate_fields(email, password, username)
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def __validate_fields(self, email: str, password: str, username: str):
        if not email:
            raise ValueError("Email address must be provided")
        if not password:
            raise ValueError("Password must be provided")
        if not username:
            raise ValueError("Username must be provided")


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserAccountManager()

    REQUIRED_FIELDS = ["username"]
    USERNAME_FIELD = "email"

    username = models.CharField("Юзейрнейм", unique=True, max_length=16)
    email = models.EmailField("E-mail", unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_verified = models.BooleanField("Проверка почты", default=False)
    is_staff = models.BooleanField("staff status", default=False)
    is_active = models.BooleanField("active", default=True)

    def set_password(self, raw_password: str | None) -> None:
        return super().set_password(raw_password)