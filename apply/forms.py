from django.forms import ModelForm
from .models import Application


class JobApplicationForm(ModelForm):
    class Meta:
        model = Application
        exclude = 'job_id', 'app_id', 'candidate', 'submit_date', 'status'

    """
    def clean_job_id(self):
        job_id = self.cleaned_data["job_id"]
        candidate = self.cleaned_data["candidate"]

        applications_already_open = Application.objects.filter(email=candidate, job_id=job_id)
        if applications_already_open.count() > 0:
            raise ValidationError("Application already exists")
        return job_id
    """