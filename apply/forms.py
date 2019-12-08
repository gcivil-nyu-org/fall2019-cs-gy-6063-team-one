from django.forms import ModelForm, BooleanField
from uplyft.models import CandidateProfile
import file_resubmit.widgets
from django.forms.widgets import ClearableFileInput
from django.core.exceptions import ValidationError


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
            "resume": "Allowed file types: .pdf, .doc, .docx <br/> \
            Max file size: 2 MiB",
            "cover_letter": "Allowed file types: .pdf, .doc, .docx <br/> Max "
            "file size: 2 MiB",
        }

        widgets = {
            "resume": ClearableFileInput(
                attrs={
                    "accept": "application/pdf, application/msword, "
                    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                }
            ),
            "cover_letter": file_resubmit.widgets.ResubmitFileWidget(
                attrs={
                    "accept": "application/pdf, application/msword, "
                    "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                }
            ),
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

    def clean_first_name(self):
        first_name = (
            self.cleaned_data["first_name"][:1].upper()
            + self.cleaned_data["first_name"][1:]
        )
        if not first_name.isalpha():
            raise ValidationError("First name should contain only letters (A-Z).")
        return first_name

    def clean_last_name(self):
        last_name = (
            self.cleaned_data["last_name"][:1].upper()
            + self.cleaned_data["last_name"][1:]
        )
        if not last_name.isalpha():
            raise ValidationError("Last name should contain only letters (A-Z).")
        return last_name
