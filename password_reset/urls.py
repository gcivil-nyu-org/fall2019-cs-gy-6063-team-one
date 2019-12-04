from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy
from password_reset.forms import EmailValidationOnForgotPassword

app_name = "password_reset"
urlpatterns = [
    # ex: /password_reset
    path(
        "",
        auth_views.PasswordResetView.as_view(
            template_name="password_reset/password_reset.html",
            email_template_name="password_reset/password_reset_email.html",
            success_url=reverse_lazy("password_reset:password_reset_done",),
            form_class=EmailValidationOnForgotPassword,
        ),
        name="password_reset",
    ),
    path(
        "done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="password_reset/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="password_reset/password_reset_confirm.html",
            success_url=reverse_lazy("password_reset:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),
    path(
        "complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="password_reset/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
