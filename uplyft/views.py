from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import get_user_model
from .forms import CandidateRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.utils.translation import ugettext_lazy as _

class IndexView(generic.ListView):
    template_name = 'uplyft/index.html'


def register(request): 
    if request.method == 'POST':
        form = CandidateRegistrationForm(request.POST)
        if form.is_valid():
        	user = form.save(commit=True)
        	email = form.cleaned_data.get('email')
        	password = form.cleaned_data.get('password1')
        	user.save()
        	user = authenticate(email=email, password=password)
        	login(request, user)
        	messages.success(request, 'Account created successfully')
        	return HttpResponseRedirect('uplyft/')
        else: 
        	form = CandidateRegistrationForm()
    else:
        form = CandidateRegistrationForm()
    return render(request, 'uplyft/register.html', {'form': form})



