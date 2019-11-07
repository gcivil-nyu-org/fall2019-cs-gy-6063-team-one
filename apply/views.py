from django.contrib import messages
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from jobs.models import Job
from django.shortcuts import render, redirect
from .forms import ApplicationForm
from .models import Application
from uplyft.models import Candidate


def apply(request, pk):
    candidate = Candidate.objects.get(user=request.user)
    if request.method == "POST":
        application = ApplicationForm(request.POST, instance=candidate)
        if application.is_valid():
            updated_profile = application.save()
            candidate.candidate_profile = updated_profile
            candidate.save()
            messages.success(request, _("Your profile was successfully updated"))
            return redirect("candidate_profile:profile")
        else:
            messages.error(request, _("Please correct the error below."))
    else:
        application = ApplicationForm(instance=candidate)
        job = Job.objects.get(pk=pk)
        return render(request, "apply/apply.html", {"application": application, "job": job, "candidate": candidate})

    # if request.method == "POST":
    #     pass
    #     # form = JobApplicationForm(request.POST)
    #     # jobs_pk_id = request.POST.get("jobs_pk_id")
    #     # email = request.session["email"]
    #     # if form.is_valid():
    #     #     user = get_user_model().objects.get(email=email)
    #     #     candidate = Candidate.objects.get(user=user)
    #     #     job = Job.objects.get(pk=jobs_pk_id)
    #     #     application = Application(job=job, candidate=candidate)
    #     #     application.save()
    #     #     messages.success(request, "Application submitted")
    #     # return HttpResponseRedirect(
    #     #     reverse("jobs:job_detail", kwargs={"pk": jobs_pk_id})
    #     # )
    # else:
    #     # email = request.session["email"]
    #     # user = get_user_model().objects.get(email=email)


