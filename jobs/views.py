import logging
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.db.models import Q
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
    filterset_class = JobFilter
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
                | Q(job_description__icontains=a)
                | Q(civil_service_title__icontains=a)
                | Q(job_category__icontains=a)
                | Q(division__icontains=a)
                | Q(min_qualifications__icontains=a)
                | Q(additional_info__icontains=a)
                | Q(id__iexact=a)
            ).order_by("-posting_date")
        else:
            queryset = Job.objects.all().order_by("-posting_date")
        return queryset

    # Loads jobs_applied context object, which is used to display either "Apply
    # now" or "Application submitted" within each job card depending on whether the
    # candidate already has a pending application or not
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["user"] = user
        if user.is_candidate:
            candidate = Candidate.objects.get(user=self.request.user)
            context["jobs_applied"] = list(
                Application.objects.filter(candidate=candidate).values_list(
                    "job", flat=True
                )
            )
        return context


class JobAdvancedSearchView(LoginRequiredMixin, ListView, FilterView):
    filterset_class = JobFilter
    model = Job
    paginate_by = 10
    context_object_name = "jobs"
    template_name = "jobs/jobs_advanced_search.html"

    def get_queryset(self):
        queryset = Job.objects.all().order_by("-posting_date")
        self.filterset = JobFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs.distinct()

    # Loads jobs_applied context object, which is used to display either "Apply
    # now" or "Application submitted" within each job card depending on whether the
    # candidate already has a pending application or not
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["user"] = user
        if user.is_candidate:
            candidate = Candidate.objects.get(user=self.request.user)
            context["jobs_applied"] = list(
                Application.objects.filter(candidate=candidate).values_list(
                    "job", flat=True
                )
            )
        context["form"] = self.filterset.form
        return context


class JobDetailView(LoginRequiredMixin, DetailView):
    model = Job
    template_name = "jobs/job_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        job = Job.objects.get(id=self.kwargs.get("pk"))
        user = self.request.user
        context["user"] = user
        context["messages"] = None

        if user.is_candidate:
            context["candidate_viewing"] = True
            candidate = Candidate.objects.get(user=user)
            context["open_applications"] = Application.objects.filter(
                candidate=candidate, job=job
            )
            if context["open_applications"].count() > 0:
                context["application_id"] = context["open_applications"][0].id
            context["saved_this_job"] = (
                SavedJobs.objects.filter(user=user, job=job).count() > 0
            )

            # Get the applications that have been submitted for this job by other people
            apps = Application.objects.filter(job=job).exclude(candidate=candidate)
            # Count how many unique applicants there are across those applications
            other_applicants = apps.values("candidate").distinct().count()

            # Pass the number of applications into context
            context["other_applicants"] = other_applicants

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
    if records.count() == 0:
        bookmark = SavedJobs(user=user, job=job)
        bookmark.save()
    else:
        records.delete()

    return HttpResponseRedirect(reverse("jobs:job_detail", kwargs={"pk": pk}))
