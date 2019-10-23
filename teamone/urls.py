"""teamone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from candidate_login.views import login_success
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("uplyft/", include("uplyft.urls")),
    path("admin/", admin.site.urls),
    path("register/", include("register.urls")),
    path("jobs/", include("jobs.urls")),
    path("candidate_login/", include("candidate_login.urls")),
    path("employer_login/", include("employer_login.urls")),
    path("accounts/", include("allauth.urls")),
    path("accounts/google/login/callback/success/",login_success),
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="candidate_login/password_reset.html"
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="candidate_login/password_reset_done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="candidate_login/password_reset_confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset-complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="candidate_login/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),

]
