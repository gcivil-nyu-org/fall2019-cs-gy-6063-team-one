from django.contrib import messages
from django.contrib.auth.decorators import login_required

from jobs.models import Job
from django.utils.translation import gettext as _
from django.shortcuts import render, redirect

from uplyft.decorators import candidate_login_required
from .forms import ApplicationForm
from .models import Application
from uplyft.models import Candidate, ActiveProfile


@login_required
@candidate_login_required
def apply(request, pk):
    candidate = Candidate.objects.get(user=request.user)
    active_prof = ActiveProfile.objects.get(candidate=candidate)
    current_res = active_prof.candidate_profile.resume

    # request.FILES is a dictionary that holds the files the candidate uploaded
    if request.method == "POST":
        if request.FILES == {}:  # The candidate uploaded no files
            # The candidate wants to use their existing resume (and no cover letter)
            file_data = {"resume": active_prof.candidate_profile.resume}
            application = ApplicationForm(request.POST, file_data, initial={"resume": current_res})
        elif "resume" not in request.FILES and "cover_letter" in request.FILES:
            # The candidate wants to use their existing resume (and a new cover letter)
            file_data = {
                "resume": active_prof.candidate_profile.resume,
                "cover_letter": request.FILES["cover_letter"],
            }
            application = ApplicationForm(request.POST, file_data, initial={"resume": current_res})
        else:
            # The candidate provides either a new resume and a new
            # cover letter (or just a new resume)
            application = ApplicationForm(request.POST, request.FILES, initial={"resume": current_res})
        job = Job.objects.get(pk=pk)

        application_in_database = (
            Application.objects.filter(job=job)
            .filter(candidate=candidate)
            .filter(status="AC")
        )
        if application_in_database.count() > 0:
            return redirect("errors:forbidden")

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
            messages.error(request, _("Please correct the error(s) below."))
            return render(
                request,
                "apply/apply.html",
                {"application": application, "job": job, "candidate": candidate},
            )
    else:
        application = ApplicationForm(instance=active_prof.candidate_profile)
        job = Job.objects.get(pk=pk)
        return render(
            request,
            "apply/apply.html",
            {"application": application, "job": job, "candidate": candidate},
        )
