from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.views import LoginView, LogoutView
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from .forms import CandidateLoginForm


@receiver(user_logged_in)
def set_session(sender, user, request, **kwargs):
    request.session["email"] = user.email


user_logged_in.connect(set_session)


class CandidateLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "candidate_login/candidate_login.html"
    authentication_form = CandidateLoginForm


def user_dashboard(request):
    return render(request, "candidate_login/dashboard.html")


def login_success(request):
    return HttpResponseRedirect(reverse("candidate_login:user_dashboard"))


class CandidateLogoutView(LogoutView):
    next_page = "uplyft:index"
    template_name = "candidate_login/candidate_logout.html"
