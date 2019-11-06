from django.urls import path

from . import views

app_name = "employer_login"
urlpatterns = [
    # ex: /employer_login
    path("", views.EmployerLoginView.as_view(), name="employer_login"),
    path("success/", views.login_success, name="success"),
]
