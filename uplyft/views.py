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


