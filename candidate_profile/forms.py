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

    def __init__(self, *args, **kwargs):
        candidate = kwargs.pop("instance")
        super(CandidateProfileForm, self).__init__(*args, **kwargs)
        """
        Initialize the form so it contains the
        information the user has already provided
        """
        # Make sure the first letter of the user's first and last name are capitalize
        self.fields["first_name"].initial = (
            candidate.candidate_profile.first_name[:1].upper()
            + candidate.candidate_profile.first_name[1:]
        )
        self.fields["last_name"].initial = (
            candidate.candidate_profile.last_name[:1].upper()
            + candidate.candidate_profile.last_name[1:]
        )
        self.fields["address_line"].initial = candidate.candidate_profile.address_line
        self.fields["zip_code"].initial = candidate.candidate_profile.zip_code
        self.fields["state"].initial = candidate.candidate_profile.state
        self.fields["email"].initial = candidate.candidate_profile.email
        self.fields["phone"].initial = candidate.candidate_profile.phone
        self.fields[
            "portfolio_website"
        ].initial = candidate.candidate_profile.portfolio_website
        self.fields["education"].initial = candidate.candidate_profile.education
        self.fields["experiences"].initial = candidate.candidate_profile.experiences
        self.fields["cover_letter"].initial = candidate.candidate_profile.cover_letter
        self.fields["gender"].initial = candidate.candidate_profile.gender
        self.fields["ethnicity"].initial = candidate.candidate_profile.ethnicity
        self.fields["race"].initial = candidate.candidate_profile.race
        self.fields[
            "health_conditions"
        ].initial = candidate.candidate_profile.health_conditions
        self.fields["veteran"].initial = candidate.candidate_profile.veteran
