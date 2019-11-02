from django.urls import path

from . import views

app_name = "register"
urlpatterns = [
    path("candidate_register", views.candidate_register, name="candidate_register"),
    path("employer_register", views.employer_register, name="employer_register"),
]
