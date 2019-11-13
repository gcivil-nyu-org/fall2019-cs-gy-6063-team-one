from django import forms
from uplyft.models import CandidateProfile, ActiveProfile
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

    def __init__(self, *args, **kwargs):
        candidate = kwargs.pop("instance")
        active_prof = ActiveProfile.objects.get(candidate=candidate)
        super(CandidateProfileForm, self).__init__(*args, **kwargs)
        """
        Initialize the form so it contains the
        information the user has already provided
        """
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["email"].required = True

        # Make sure the first letter of the user's first and last name are capitalized
        self.fields["first_name"].initial = (
            active_prof.candidate_profile.first_name[:1].upper()
            + active_prof.candidate_profile.first_name[1:]
        )

        self.fields["last_name"].initial = (
            active_prof.candidate_profile.last_name[:1].upper()
            + active_prof.candidate_profile.last_name[1:]
        )

        self.fields["address_line"].initial = active_prof.candidate_profile.address_line
        self.fields["zip_code"].initial = active_prof.candidate_profile.zip_code
        self.fields["state"].initial = active_prof.candidate_profile.state
        self.fields["email"].initial = active_prof.candidate_profile.email
        self.fields["phone"].initial = active_prof.candidate_profile.phone
        self.fields[
            "portfolio_website"
        ].initial = active_prof.candidate_profile.portfolio_website
        self.fields["education"].initial = active_prof.candidate_profile.education
        self.fields["experiences"].initial = active_prof.candidate_profile.experiences
        self.fields["cover_letter"].initial = active_prof.candidate_profile.cover_letter
        self.fields["gender"].initial = active_prof.candidate_profile.gender
        self.fields["ethnicity"].initial = active_prof.candidate_profile.ethnicity
        self.fields["race"].initial = active_prof.candidate_profile.race
        self.fields[
            "health_conditions"
        ].initial = active_prof.candidate_profile.health_conditions
        self.fields["veteran"].initial = active_prof.candidate_profile.veteran