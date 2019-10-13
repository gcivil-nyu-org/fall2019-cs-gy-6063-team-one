from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import views as auth_views
from .forms import EmployerLoginForm


class EmployerLoginView(auth_views.LoginView):
    template_name = 'employer_login/employer_login.html'
    authentication_form = EmployerLoginForm


def login_success(request):
    if request.user.is_authenticated:
        name = request.user.first_name
        if name == '' or name is None:
            name = request.user.username
        messages.success(request, 'Hi, ' + name + '!')
    else:
        HttpResponseRedirect('employer_login:employer_login')
    return render(request, 'employer_login/employer_login_success.html')