from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.views import LoginView, LogoutView
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CandidateLoginForm


class CandidateLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "candidate_login/candidate_login.html"
    authentication_form = CandidateLoginForm


def login_success(request):
    return HttpResponseRedirect(reverse("jobs:jobs"))


class CandidateLogoutView(LogoutView):
    next_page = "uplyft:index"
    template_name = "candidate_login/candidate_logout.html"
