from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from uplyft.decorators import candidate_login_required
from uplyft.models import Candidate, ActiveProfile
from django.contrib import messages
from .forms import CandidateProfileForm
from django.db import transaction


# Create your views here.
@login_required
@candidate_login_required
@transaction.atomic
def update_candidate_profile(request):
    candidate = Candidate.objects.get(user=request.user)
    active_profile = ActiveProfile.objects.get(candidate=candidate)

    if request.method == "POST":
        profile_form = CandidateProfileForm(
            request.POST, request.FILES, instance=active_profile.candidate_profile
        )
        if profile_form.is_valid():
            updated_profile = profile_form.save()
            active_profile.candidate_profile = updated_profile
            active_profile.save()
            messages.success(request, _("Your profile was successfully updated"))
            return redirect("candidate_profile:profile")
        else:
            messages.error(request, _("Please correct the error(s) below."))
            return render(
                request,
                "candidate_profile.html",
                {
                    "profile_form": profile_form,
                    "candidate": candidate,
                    "active_profile": active_profile,
                },
            )
    else:
        profile_form = CandidateProfileForm(instance=active_profile.candidate_profile)
        return render(
            request,
            "candidate_profile.html",
            {
                "profile_form": profile_form,
                "candidate": candidate,
                "active_profile": active_profile,
            },
        )
