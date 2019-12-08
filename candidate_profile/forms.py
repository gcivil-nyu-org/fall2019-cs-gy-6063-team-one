from django import forms
from uplyft.models import CandidateProfile
import file_resubmit.widgets
from django.core.exceptions import ValidationError


class CandidateProfileForm(forms.ModelForm):
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
            "gender",
            "ethnicity",
            "race",
            "health_conditions",
            "veteran",
        )

        widgets = {
            "resume": file_resubmit.widgets.ResubmitFileWidget(
                attrs={
                    "accept": "application/pdf, application/msword,"
                    " application/vnd.openxmlformats-officedocument."
                              "wordprocessingml.document"
                }
            )
        }
        help_texts = {
            "resume": "Allowed file types: .pdf, .doc, .docx <br/> "
            "Max file size: 2 MiB"
        }

    # Make name and email always be mandatory
    def __init__(self, *args, **kwargs):
        super(CandidateProfileForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["email"].required = True
        self.fields["resume"].required = False

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
