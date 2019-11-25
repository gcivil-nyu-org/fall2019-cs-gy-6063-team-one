from django.shortcuts import render, redirect
from django.utils.translation import gettext as _
from uplyft.decorators import candidate_login_required
from uplyft.models import Candidate, ActiveProfile
from django.contrib import messages
from .forms import CandidateProfileForm
from django.db import transaction

# Create your views here.
@candidate_login_required
@transaction.atomic
def update_candidate_profile(request):
    candidate = Candidate.objects.get(user=request.user)
    active_profile = ActiveProfile.objects.get(candidate=candidate)

    # Pre-populate the profile with the information the candidate has already provided
    # Make sure the first letter of the user's first and last name are capitalized
    default_data = {
        "first_name": active_profile.candidate_profile.first_name[:1].upper()
        + active_profile.candidate_profile.first_name[1:],
        "last_name": active_profile.candidate_profile.last_name[:1].upper()
        + active_profile.candidate_profile.last_name[1:],
        "address_line": active_profile.candidate_profile.address_line,
        "zip_code": active_profile.candidate_profile.zip_code,
        "state": active_profile.candidate_profile.state,
        "email": active_profile.candidate_profile.email,
        "phone": active_profile.candidate_profile.phone,
        "portfolio_website": active_profile.candidate_profile.portfolio_website
        if active_profile.candidate_profile.portfolio_website
        else "http://",
        "education": active_profile.candidate_profile.education,
        "experiences": active_profile.candidate_profile.experiences,
        "cover_letter": active_profile.candidate_profile.cover_letter,
        "gender": active_profile.candidate_profile.gender,
        "ethnicity": active_profile.candidate_profile.ethnicity,
        "race": active_profile.candidate_profile.race,
        "health_conditions": active_profile.candidate_profile.health_conditions,
        "veteran": active_profile.candidate_profile.veteran,
    }

    if request.method == "POST":
        profile_form = CandidateProfileForm(request.POST)
        if profile_form.is_valid():
            updated_profile = profile_form.save()
            active_profile.candidate_profile = updated_profile
            active_profile.save()
            messages.success(request, _("Your profile was successfully updated"))
            return redirect("candidate_profile:profile")
        else:
            messages.error(request, _("Please correct the error below."))
    else:
        profile_form = CandidateProfileForm(default_data)
        return render(
            request,
            "candidate_profile.html",
            {"profile_form": profile_form, "candidate": candidate},
        )
