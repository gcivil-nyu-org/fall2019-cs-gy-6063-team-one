from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView

from apply.models import Application
from jobs.models import Job
from uplyft.models import Candidate, Employer

ALL = "ALL"


@login_required
def dashboard(request):
    if request.user.is_active:
        if request.user.is_candidate:
            return handle_candidate_dashboard(request)
        else:
            return handle_employer_dashboard(request)
    else:
        return HttpResponseRedirect(reverse("errors:forbidden"))


class ApplicationList(LoginRequiredMixin, ListView):
    model = Application
    paginate_by = 10
    context_object_name = "applications"
    template_name = "dashboard/applications_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        app_status = self.kwargs["app_status"]
        context["application_type"] = app_status
        if self.request.user.is_candidate:
            context["employer_viewing"] = False
        else:
            context["employer_viewing"] = True
        return context

    def get_candidate_applications(self, app_status):
        candidate = Candidate.objects.filter(user=self.request.user)
        try:
            candidate_applications = Application.objects.filter(
                candidate=candidate[0]
            ).order_by("-submit_date")
        except Application.DoesNotExist:
            return []
        if app_status and app_status != ALL:
            candidate_applications = candidate_applications.filter(
                status=app_status
            ).order_by("-submit_date")
        try:
            query = self.request.GET.get("q")
        except KeyError:
            query = None
        if query:
            candidate_applications = candidate_applications.filter(
                Q(job__business_title__icontains=query)
                | Q(candidate_profile__first_name__icontains=query)
                | Q(candidate_profile__last_name__icontains=query)
            ).order_by("-submit_date")
        return candidate_applications

    def get_employer_applications(self, app_status):
        employer = Employer.objects.get(user=self.request.user)
        try:
            jobs = Job.objects.filter(department=employer.department)
        except Job.DoesNotExist:
            return []
        try:
            employer_applications = Application.objects.filter(job__in=jobs).order_by(
                "-submit_date"
            )
        except Application.DoesNotExist:
            return []
        if app_status and app_status != ALL:
            employer_applications = employer_applications.filter(
                status=app_status
            ).order_by("-submit_date")
        try:
            query = self.request.GET.get("q")
        except KeyError:
            query = None
        if query:
            employer_applications = employer_applications.filter(
                Q(job__business_title__contains=query)
                | Q(candidate_profile__first_name__contains=query)
                | Q(candidate_profile__last_name__contains=query)
            ).order_by("-submit_date")
        return employer_applications

    def get_queryset(self):
        if self.request.user.is_active:
            app_status = self.kwargs["app_status"]
            app_status = app_status.upper()
            if app_status not in [
                Application.STATUS_ACCEPTED,
                Application.STATUS_REJECTED,
                Application.STATUS_APPLIED,
                ALL,
            ]:
                app_status = None
            if self.request.user.is_candidate:
                return self.get_candidate_applications(app_status)
            else:
                return self.get_employer_applications(app_status)


def handle_candidate_dashboard(request):
    candidate = Candidate.objects.filter(user=request.user)
    try:
        candidate_applications = Application.objects.filter(candidate=candidate[0])
    except Application.DoesNotExist:
        candidate_applications = None

    candidate = candidate[0]
    candidate_name = candidate.candidate_profile.first_name

    accepted_count = 0
    rejected_count = 0
    pending_count = 0
    if candidate_applications:
        accepted_count = candidate_applications.filter(
            status=Application.STATUS_ACCEPTED
        ).count()
        rejected_count = candidate_applications.filter(
            status=Application.STATUS_REJECTED
        ).count()
        pending_count = candidate_applications.filter(
            status=Application.STATUS_APPLIED
        ).count()
    context = {
        "candidate_name": candidate_name,
        "accepted_count": accepted_count,
        "rejected_count": rejected_count,
        "pending_count": pending_count,
    }
    return render(request, "dashboard/candidate_dashboard.html", context=context)


def handle_employer_dashboard(request):
    employer = Employer.objects.get(user=request.user)
    try:
        jobs = Job.objects.filter(department=employer.department)
    except Job.DoesNotExist:
        jobs = None
    accepted_count = 0
    rejected_count = 0
    pending_count = 0
    if jobs:
        try:
            employer_applications = Application.objects.filter(job__in=jobs)
        except Application.DoesNotExist:
            employer_applications = None
        if employer_applications:
            accepted_count = employer_applications.filter(
                status=Application.STATUS_ACCEPTED
            ).count()
            rejected_count = employer_applications.filter(
                status=Application.STATUS_REJECTED
            ).count()
            pending_count = employer_applications.filter(
                status=Application.STATUS_APPLIED
            ).count()
    context = {
        "employer_name": employer.user.first_name,
        "accepted_count": accepted_count,
        "rejected_count": rejected_count,
        "pending_count": pending_count,
    }
    return render(request, "dashboard/employer_dashboard.html", context=context)
