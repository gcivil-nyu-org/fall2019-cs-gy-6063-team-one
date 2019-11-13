from django import forms
from uplyft.models import CandidateProfile
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
            "education",
            "experiences",
            "cover_letter",
            "gender",
            "ethnicity",
            "race",
            "health_conditions",
            "veteran",
        )

    # Make name and email always be mandatory
    def __init__(self, *args, **kwargs):
        super(CandidateProfileForm, self).__init__(*args, **kwargs)
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["email"].required = True

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"].lower()
        if not first_name.isalpha():
            raise ValidationError("First name should contain only letters (A-Z).")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"].lower()
        if not last_name.isalpha():
            raise ValidationError("Last name should contain only letters (A-Z).")
        return last_name
