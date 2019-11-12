from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import EmployerLoginForm


class EmployerLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "employer_login/employer_login.html"
    authentication_form = EmployerLoginForm


def login_success(request):
    if request.user.is_authenticated:
        return render(request, "employer_login/employer_login_success.html")
    else:
        return HttpResponseRedirect("employer_login:employer_login")



class EmployerLogoutView(LogoutView):
    next_page = "uplyft:index"
    template_name = "employer_login/employer_logout.html"
