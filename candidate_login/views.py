from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.views import LoginView, LogoutView
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from uplyft.decorators import candidate_login_required
from .forms import CandidateLoginForm, CandidateProfileForm
from uplyft.models import Candidate
from django.contrib import messages
from django.db import transaction


@receiver(user_logged_in)
def set_session(sender, user, request, **kwargs):
    request.session["email"] = user.email


user_logged_in.connect(set_session)


class CandidateLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "candidate_login/candidate_login.html"
    authentication_form = CandidateLoginForm


# Ensure a candidate is logged in before they can view their dashboard or profile


def candidate_dashboard(request):
    return render(request, "candidate_login/dashboard.html")


@candidate_login_required
@transaction.atomic
def update_candidate_profile(request):
    candidate = Candidate.objects.get(user=request.user)
    if request.method == "POST":
        profile_form = CandidateProfileForm(request.POST, instance=candidate)
        if profile_form.is_valid():
            updated_profile = profile_form.save()
            candidate.candidate_profile = updated_profile
            candidate.save()
            messages.success(request, _("Your profile was successfully updated"))
            return redirect("candidate_login:candidate_profile")
        else:
            messages.error(request, _("Please correct the error below."))
    else:
        profile_form = CandidateProfileForm(instance=candidate)
        return render(
            request,
            "candidate_login/profile.html",
            {"profile_form": profile_form, "candidate": candidate},
        )


def login_success(request):
    return HttpResponseRedirect(reverse("candidate_login:user_dashboard"))


class CandidateLogoutView(LogoutView):
    next_page = "uplyft:index"
    template_name = "candidate_login/candidate_logout.html"
