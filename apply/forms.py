from django.forms import ModelForm, ValidationError
from .models import Application
from jobs.models import Job
from django.contrib.auth import get_user_model


class JobApplicationForm(ModelForm):
    class Meta:
        model = Application
        exclude = (
            "job_id",
            "job",
            "application_id",
            "candidate",
            "submit_date",
            "status",
        )

    def clean_active_application_already_exists(self):
        job_id = self.cleaned_data["job_id"]
        email = self.request.session["email"]
        user = get_user_model().objects.get(email=email)
        job = Job.objects.get(pk=job_id)
        active_application_exists = Application.objects.filter(
            job=job, candidate=user, status="ACTIVE"
        )
        if active_application_exists.count() > 0:
            raise ValidationError(
                "Candidate has already submitted an ACTIVE application for this job."
            )
