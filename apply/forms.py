from django.forms import ModelForm, BooleanField
from uplyft.models import CandidateProfile
import file_resubmit.widgets
from django.forms.widgets import ClearableFileInput


class ApplicationForm(ModelForm):
    # Check box for whether the user wants to push changes to their profile
    update_profile = BooleanField(required=False, initial=False)

    class Meta:
        model = CandidateProfile
        fields = (
            "first_name",
            "last_name",
            "address_line",
            "zip_code",
            "state",
            "email",
            "phone",
            "portfolio_website",
            "resume",
            "cover_letter",
            "gender",
            "ethnicity",
            "race",
            "health_conditions",
            "veteran",
            "update_profile",
        )

        help_texts = {
            "resume": "Allowed file types: .pdf, .doc, .docx <br/> Max file size: 2 MiB",
            "cover_letter": "Allowed file types: .pdf, .doc, .docx <br/> Max "
            "file size: 2 MiB",
        }

        widgets = {"resume": ClearableFileInput(attrs={
                    "accept": "application/pdf, application/msword, \
                    application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                }),
            "cover_letter": file_resubmit.widgets.ResubmitFileWidget(
                attrs={
                    "accept": "application/pdf, application/msword, \
                    application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                }
            )
        }

    def __init__(self, *args, **kwargs):
        super(ApplicationForm, self).__init__(*args, **kwargs)

        # Set some of the fields to be required
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["address_line"].required = True
        self.fields["zip_code"].required = True
        self.fields["state"].required = True
        self.fields["email"].required = True
        self.fields["phone"].required = True
        self.fields["resume"].required = True
        self.fields["cover_letter"].required = False

    # def clean_active_application_already_exists(self):
    #     jobs_pk_id = self.cleaned_data["jobs_pk_id"]
    #     email = self.request.session["email"]
    #     user = get_user_model().objects.get(email=email)
    #     candidate = Candidate.objects.get(user=user)
    #     job = Job.objects.get(pk=jobs_pk_id)
    #     active_application_exists = Application.objects.filter(
    #         job=job, candidate=candidate, status="ACTIVE"
    #     )
    #     if active_application_exists.count() > 0:
    #         raise ValidationError(
    #             "Candidate has already submitted an ACTIVE application for this job."
    #         )
