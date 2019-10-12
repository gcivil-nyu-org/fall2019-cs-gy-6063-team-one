from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import messages

# Authentication
from django.contrib.auth import authenticate, login
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


# Uplyft imports
from .forms import UplyftCandidateLoginForm

class IndexView(generic.ListView):
    template_name = 'uplyft/index.html'

# Login

class UplyftCandidateLoginView(auth_views.LoginView):
	template_name = 'uplyft/registration/experimental_login.html'
	authentication_form = UplyftCandidateLoginForm

# def uplyft_candidate_login(request):
# 	if request.user.is_authenticated:
# 		return HttpResponseRedirect('confetti/')

# 	if request.method == 'POST':
# 		username = request.POST['username']
# 		password = request.POST['password']
# 		user = authenticate(request, username=username, password=password)
# 		if user is not None:
# 			login(request, user)
# 			# Redirect to a success page
# 			return HttpResponseRedirect('confetti/')
# 		else:
# 			messages.warning(request, 'The login is not successful.')
# 			needs_login_form = True
# 	elif request.method == 'GET':
# 		needs_login_form = True

# 	login_form = UplyftCandidateLoginForm()
# 	return render(request, 'uplyft/registration/experimental_login.html', {'form': login_form})

def login_confetti(request):
	if request.user.is_authenticated:
		name = request.user.first_name
		if name == '' or name is None:
			name = request.user.username
		messages.success(request, 'Hi, ' + name + '!')
	else:
		HttpResponseRedirect('uplyft:login')
	return render(request, 'uplyft/registration/login_success.html', {})
