from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from apply.models import Application
from jobs.models import Job
from uplyft.models import Candidate, Employer


@login_required
def dashboard(request):
    if request.user.is_active:
        if request.user.is_candidate:
            return handle_candidate(request)
        else:
            return handle_employer(request)


def handle_candidate(request):
    candidate = Candidate.objects.filter(user=request.user)
    try:
        candidate_applications = Application.objects.filter(candidate=candidate[0])
    except Application.DoesNotExist:
        candidate_applications = None

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
        "accepted_count": accepted_count,
        "rejected_count": rejected_count,
        "pending_count": pending_count,
    }
    return render(request, "dashboard/candidate_dashboard.html", context=context)


def handle_employer(request):
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
        "accepted_count": accepted_count,
        "rejected_count": rejected_count,
        "pending_count": pending_count,
    }
    return render(request, "dashboard/employer_dashboard.html", context=context)
