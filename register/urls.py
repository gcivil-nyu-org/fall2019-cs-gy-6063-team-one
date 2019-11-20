from django.conf.urls import url
from django.urls import path

from . import views

app_name = "register"
urlpatterns = [
    path("candidate_register", views.candidate_register, name="candidate_register"),
    path("employer_register", views.employer_register, name="employer_register"),
    url(
        r"activate/(?P<uidb64>[0-9A-Za-z_\-]+)/,(?P<token>[0-9A-Za-z]{1,13}"
        r"-[0-9A-Za-z]{1,20})/$",
        views.activate_account,
        name="activate",
    ),
    path(
        "email_confirmation", views.email_confirmation_sent, name="email_confirmation"
    ),
]
