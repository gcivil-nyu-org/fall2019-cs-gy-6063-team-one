from django.contrib import messages
from jobs.models import Job
from django.utils.translation import gettext as _
from django.shortcuts import render, redirect
from .forms import ApplicationForm
from .models import Application
from uplyft.models import Candidate, ActiveProfile


def apply(request, pk):
    candidate = Candidate.objects.get(user=request.user)
    active_prof = ActiveProfile.objects.get(candidate=candidate)

    default_data = {
        "first_name": active_prof.candidate_profile.first_name[:1].upper()
        + active_prof.candidate_profile.first_name[1:],
        "last_name": active_prof.candidate_profile.last_name[:1].upper()
        + active_prof.candidate_profile.last_name[1:],
        "address_line": active_prof.candidate_profile.address_line,
        "zip_code": active_prof.candidate_profile.zip_code,
        "state": active_prof.candidate_profile.state,
        "email": active_prof.candidate_profile.email,
        "phone": active_prof.candidate_profile.phone,
        "portfolio_website": active_prof.candidate_profile.portfolio_website,
        "education": active_prof.candidate_profile.education,
        "experiences": active_prof.candidate_profile.experiences,
        "cover_letter": active_prof.candidate_profile.cover_letter,
        "gender": active_prof.candidate_profile.gender,
        "ethnicity": active_prof.candidate_profile.ethnicity,
        "race": active_prof.candidate_profile.race,
        "health_conditions": active_prof.candidate_profile.health_conditions,
        "veteran": active_prof.candidate_profile.veteran,
        "update_profile": False,
    }

    if request.method == "POST":
        application = ApplicationForm(request.POST, request.FILES)
        job = Job.objects.get(pk=pk)

        if application.is_valid():

            # Get the candidate's active profile
            candidate_prof = active_prof.candidate_profile

            # If the user says to update their profile
            if application.cleaned_data.get("update_profile"):

                # If user only checked the box, but didn't change any other fields
                if application.changed_data == [
                    "update_profile"
                ]:  # No actual changes to any fields
                    # Load the active profile into the current application and submit
                    app_obj = Application(
                        job=job, candidate=candidate, candidate_profile=candidate_prof
                    )
                    app_obj.save()

                else:  # If they changed fields besides the check box

                    # Check if any other applications use the active profile
                    prof_in_use = False
                    if (
                        Application.objects.filter(
                            candidate_profile=candidate_prof
                        ).count()
                        > 0
                    ):
                        prof_in_use = True

                    if prof_in_use:
                        # Create a new profile, make it the active one, include it
                        # in the application
                        new_prof = application.save()
                        active_prof.candidate_profile = new_prof
                        active_prof.save()

                        app_obj = Application(
                            job=job,
                            candidate=candidate,
                            candidate_profile=active_prof.candidate_profile,
                        )
                        app_obj.save()

                    else:
                        # If the profile isn't used anywhere else, make the changes
                        # to the active profile
                        updated_prof = application.save()
                        active_prof.candidate_profile = updated_prof
                        active_prof.save()

                        # Submit the application using the active profile
                        app_obj = Application(
                            job=job, candidate=candidate, candidate_profile=updated_prof
                        )
                        app_obj.save()

            # If the user doesn't want to update their profile
            else:
                # There are no changes - submit the app with the active profile
                if not application.changed_data:
                    app_obj = Application(
                        job=job, candidate=candidate, candidate_profile=candidate_prof
                    )
                # The user made changes - submit the application with the new profile
                else:
                    new_prof = application.save()
                    app_obj = Application(
                        job=job, candidate=candidate, candidate_profile=new_prof
                    )
                app_obj.save()
            messages.success(request, "Application submitted")
            return redirect("applications:application_details", pk=app_obj.pk)
        else:
            messages.error(request, _("Please correct the error below."))
            return render(
                request,
                "apply/apply.html",
                {"application": application, "job": job, "candidate": candidate},
            )
    else:
        application = ApplicationForm(default_data)
        job = Job.objects.get(pk=pk)
        return render(
            request,
            "apply/apply.html",
            {"application": application, "job": job, "candidate": candidate},
        )
