from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from .forms import EmployerLoginForm
from uplyft.decorators import employer_login_required


class EmployerLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "employer_login/employer_login.html"
    authentication_form = EmployerLoginForm


@employer_login_required
def login_success(request):
    if request.user.is_authenticated:
        name = request.user.first_name
        if name == "" or name is None:
            name = request.user.username
        messages.success(request, "Hi, " + name + "!")
    else:
        HttpResponseRedirect("employer_login:employer_login")
    return render(request, "employer_login/employer_login_success.html")


@employer_login_required
class EmployerLogoutView(LogoutView):
    next_page = "uplyft:index"
    template_name = "employer_login/employer_logout.html"
