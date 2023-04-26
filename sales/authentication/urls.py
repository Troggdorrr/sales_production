from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import SignUpView, LogInView, LogOutView, ResetPasswordView, ChangePasswordView


urlpatterns = [
    path("login/", LogInView.as_view()),
    path("signup/", SignUpView.as_view()),
    path("logout/", LogOutView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("reset-password/", ResetPasswordView.as_view()),
    path("change-password/", ChangePasswordView.as_view()),
]
