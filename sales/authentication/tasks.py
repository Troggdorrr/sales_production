from django.core.mail import EmailMessage

from django.contrib.auth import get_user_model
from django.conf import settings
from django.template.loader import render_to_string

from os import environ

from sales.celery import app


@app.task
def send_success_signup_email(user_pk: int) -> None:
    user = get_user_model().objects.get(pk=user_pk)
    message_text = render_to_string(
        "authentication/new_user_mail.html",
        {"username": user.username},
    )
    message = EmailMessage(
        "Успешная регистрация!",
        message_text,
        to=[user.email],
    )
    message.content_subtype = "html"
    message.send()


@app.task
def send_reset_password_email(email: str, reset_uuid: str) -> None:
    host = environ.get("HOST")
    message_text = render_to_string(
        "authentication/reset_password_mail.html",
        {"reset_link": f"{host}/reset-password?uuid={reset_uuid}"},
    )
    message = EmailMessage(
        "Восстановление пароля",
        message_text,
        to=[email],
    )
    message.content_subtype = "html"
    message.send()