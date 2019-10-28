from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from jobs.models import Job
from .forms import JobApplicationForm
from .models import Application
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required

#@login_required
def apply(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST)
        email = "username@nyc.gov"
        #  email = request.session['email']
        #  Once session component is in place

        if form.is_valid():
            user = get_user_model().objects.get(email=email)
            job = Job.objects.get(pk=87990)
            #data = form.cleaned_data
            #user = get_user_model().objects.get(email=email)
            #print(data['job_id'])
            #job = Job.objects.get(pk=data['job_id'])
            application = Application(job_id=job, candidate=user)
            application.save()
    else:
        form = JobApplicationForm()
    return render(request, "apply/apply.html", {"form": form})

