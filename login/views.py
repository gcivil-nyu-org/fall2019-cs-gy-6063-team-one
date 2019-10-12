from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import views as auth_views
from .forms import CandidateLoginForm


class CandidateLoginView(auth_views.LoginView):
    template_name = 'login/login.html'
    authentication_form = CandidateLoginForm


def login_confetti(request):
    if request.user.is_authenticated:
        name = request.user.first_name
        if name == '' or name is None:
            name = request.user.username
        messages.success(request, 'Hi, ' + name + '!')
    else:
        HttpResponseRedirect('login:login')
    return render(request, 'login/login_success.html', {})