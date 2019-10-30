from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import views as auth_views
from .forms import CandidateLoginForm
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

@receiver(user_logged_in)
def set_session(sender, user, request, **kwargs):
    request.session['email'] = user.email

user_logged_in.connect(set_session)

class CandidateLoginView(auth_views.LoginView):
    template_name = "candidate_login/candidate_login.html"
    authentication_form = CandidateLoginForm


def login_success(request):
    if request.user.is_authenticated:
        email = request.user.email
        messages.success(request, "Hi, " + email + "!")
    else:
        messages.info(request, "This page requires login.")
        return redirect("candidate_login:candidate_login")
    return render(request, "candidate_login/candidate_login_success.html")


class CandidateLogoutView(auth_views.LogoutView):
    template_name = "candidate_login/candidate_login.html"
