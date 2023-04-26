from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.conf import settings
from django.template.loader import render_to_string

from sales.celery import app


@app.task
def send_success_signup_email(user_pk: int) -> None:
    user = get_user_model().objects.get(pk=user_pk)
    message = render_to_string(
        "authentication/new_user_mail.html",
        {"username": user.username},
    )
    send_mail(
        "Успешная регистрация!",
        f"{user.username}, вы успешно зарегистрировались на сайте SaleHunter",
        settings.EMAIL_HOST_USER,
        [user.email],
        fail_silently=False,
        html_message=message
    )


@app.task
def send_reset_password_email(email: str, reset_uuid: str) -> None:
    message = render_to_string(
        "authentication/reset_password_mail.html",
        {"reset_link": f"http://localhost:2228/reset-password?uuid={reset_uuid}"},
    )
    send_mail(
        subject="Восстановление пароля",
        message=f"Ссылка для восстановления пароля: http://localhost:2228/reset-password?uuid={reset_uuid}",
        html_message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )
