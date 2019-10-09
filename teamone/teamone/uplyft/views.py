from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .models import CandidateRegistrationModel
from .forms import CandidateRegistrationForm

class IndexView(generic.ListView):
    template_name = 'uplyft/index.html'

def register(request): 
    if request.method == 'POST':
        form = CandidateRegistrationForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            return HttpResponseRedirect('/uplyft/')
    else:
        form = CandidateRegistrationForm()
        return render(request, 'uplyft/register.html', {'form': form})



