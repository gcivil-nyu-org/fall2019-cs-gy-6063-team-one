from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from jobs.models import Job
from django.shortcuts import render


from .forms import JobApplicationForm
from .models import Application
from uplyft.models import Candidate


@login_required()
def apply(request, pk):
    if request.method == "POST":
        pass
        # form = JobApplicationForm(request.POST)
        # jobs_pk_id = request.POST.get("jobs_pk_id")
        # email = request.session["email"]
        # if form.is_valid():
        #     user = get_user_model().objects.get(email=email)
        #     candidate = Candidate.objects.get(user=user)
        #     job = Job.objects.get(pk=jobs_pk_id)
        #     application = Application(job=job, candidate=candidate)
        #     application.save()
        #     messages.success(request, "Application submitted")
        # return HttpResponseRedirect(
        #     reverse("jobs:job_detail", kwargs={"pk": jobs_pk_id})
        # )
    else:
        # email = request.session["email"]
        # user = get_user_model().objects.get(email=email)
        job = Job.objects.get(pk=pk)
        return render(request, "apply/apply.html", {"job": job})
