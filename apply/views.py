from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from jobs.models import Job
from .forms import JobApplicationForm
from .models import Application
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required


@login_required
def apply(request):
    if request.method == "POST":
        form = JobApplicationForm(request.POST)
        jobs_pk_id = request.POST.get("jobs_pk_id")
        email = request.session["email"]
        if form.is_valid():
            user = get_user_model().objects.get(email=email)
            job = Job.objects.get(pk=jobs_pk_id)
            application = Application(job=job, candidate=user)
            application.save()
            messages.success(request, "Application submitted")
        return HttpResponseRedirect(
            reverse("jobs:job_detail", kwargs={"pk": jobs_pk_id})
        )
    else:
        return HttpResponseRedirect(reverse("uplyft:index"))
