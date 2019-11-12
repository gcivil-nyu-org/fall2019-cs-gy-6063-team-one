import logging

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django_filters.views import FilterView
from django.http import HttpResponseRedirect
from django.urls import reverse


from apply.models import Application
from jobs.helper import jobs_helper
from .filters import JobFilter
from .models import Job, SavedJobs
from uplyft.models import Candidate

logger = logging.getLogger(__name__)


class JobsView(LoginRequiredMixin, ListView):
    model = Job
    paginate_by = 10
    context_object_name = "jobs"
    template_name = "jobs/jobs.html"

    def get_queryset(self):
        try:
            a = self.request.GET.get("q")
        except KeyError:
            a = None
        if a:
            queryset = Job.objects.filter(
                Q(business_title__icontains=a)
                | Q(work_location__icontains=a)
                | Q(department__name__icontains=a)
            ).order_by("-posting_date")
        else:
            queryset = Job.objects.all().order_by("-posting_date")
        return queryset


class JobAdvancedSearch(LoginRequiredMixin, FilterView):
    filterset_class = JobFilter
    template_name = "jobs/job_search.html"
    paginate_by = 10
    ordering = ["-posting_date"]


class JobDetailView(LoginRequiredMixin, DetailView):
    model = Job
    template_name = "jobs/job_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        email = self.request.session["email"]
        job = Job.objects.get(id=self.kwargs.get("pk"))
        user = get_user_model().objects.get(email=email)
        context["messages"] = None

        if user.is_candidate:
            context["candidate_viewing"] = True
            candidate = Candidate.objects.get(user=user)
            context["open_applications"] = Application.objects.filter(
                candidate=candidate, job=job
            )
            context["application_id"] = context["open_applications"][0].id
            context["saved_this_job"] = (
                SavedJobs.objects.filter(user=user, job=job).count() > 0
            )

        else:
            context["candidate_viewing"] = False
            context["open_applications"] = Application.objects.none()

        if context["open_applications"].count() > 0:
            context["has_open_application"] = True
        else:
            context["has_open_application"] = False
        return context


def jobs(request):
    return render(request, "jobs/jobs.html")


def load_jobs(request):
    if request.method == "POST":
        jobs_helper.create_departments()
        jobs_helper.create_jobs()
        messages.success(request, "Jobs imported successfully")
        return render(request, "jobs/jobs_import.html")
    else:
        return render(request, "jobs/jobs_import.html")


@login_required
def save_job(request, pk):
    job = Job.objects.get(pk=pk)
    user = request.user
    records = SavedJobs.objects.filter(user=user, job=job)
    print(request)
    if records.count() == 0:
        bookmark = SavedJobs(user=user, job=job)
        bookmark.save()
    else:
        records.delete()

    return HttpResponseRedirect(reverse("jobs:job_detail", kwargs={"pk": pk}))
