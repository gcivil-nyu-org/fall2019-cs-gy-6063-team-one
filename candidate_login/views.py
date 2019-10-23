from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import views as auth_views
from .forms import CandidateLoginForm


class CandidateLoginView(auth_views.LoginView):
    template_name = "candidate_login/candidate_login.html"
    authentication_form = CandidateLoginForm


def login_success(request):
    if request.user.is_authenticated:
        email = request.user.email
        if email == "" or email is None:
            email = request.user.email
        messages.success(request, "Hi, " + email + "!")
    else:
        messages.info(request, "This page requires login.")
        return redirect("candidate_login:candidate_login")
    return render(request, "candidate_login/candidate_login_success.html")


class CandidateLogoutView(auth_views.LogoutView):
    template_name = "candidate_login/candidate_login.html"
