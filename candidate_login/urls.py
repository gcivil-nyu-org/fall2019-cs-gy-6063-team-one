from django.urls import path

from . import views

app_name = "candidate_login"
urlpatterns = [
    # ex: /candidate_login
    path("", views.CandidateLoginView.as_view(), name="candidate_login"),
    path("success/", views.login_success, name="success"),
    path("logout/", views.CandidateLogoutView.as_view(), name="candidate_logout"),
    path("dashboard/", views.candidate_dashboard, name="user_dashboard"),

]
