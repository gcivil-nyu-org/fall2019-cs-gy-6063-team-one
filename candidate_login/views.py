from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import CandidateLoginForm
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

@receiver(user_logged_in)
def set_session(sender, user, request, **kwargs):
    request.session['email'] = user.email

user_logged_in.connect(set_session)

@receiver(user_logged_in)
def set_session(sender, user, request, **kwargs):
    request.session["email"] = user.email


user_logged_in.connect(set_session)


class CandidateLoginView(auth_views.LoginView):
    redirect_authenticated_user = True
    template_name = "candidate_login/candidate_login.html"
    authentication_form = CandidateLoginForm


@login_required
def login_success(request):
    return HttpResponseRedirect(reverse("jobs:jobs"))


class CandidateLogoutView(auth_views.LogoutView):
    next_page = "uplyft:index"
    template_name = "candidate_login/candidate_logout.html"
