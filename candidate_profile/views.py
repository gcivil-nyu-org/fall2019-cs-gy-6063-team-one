from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from uplyft.decorators import candidate_login_required
from uplyft.models import Candidate
from django.contrib import messages
from .forms import CandidateProfileForm
from django.db import transaction

# Create your views here.
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
            return redirect("candidate_profile:profile")
        else:
            messages.error(request, _("Please correct the error below."))
    else:
        profile_form = CandidateProfileForm(instance=candidate)
        return render(
            request,
            "candidate_profile.html",
            {"profile_form": profile_form, "candidate": candidate},
        )
