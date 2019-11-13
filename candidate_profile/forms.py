from django import forms
from uplyft.models import CandidateProfile


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
