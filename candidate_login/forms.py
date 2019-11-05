from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from uplyft.models import CandidateProfile


class CandidateLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()

    def confirm_login_allowed(self, user):
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.

        If the given user cannot log in, this method should raise a
        ``forms.ValidationError``.

        If the user is not a Candidate, this method should raise a forms.ValidationError

        If the given user may log in, this method should return None.
        """
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages["inactive"], code="inactive"
            )

        if not user.is_candidate:
            raise forms.ValidationError(
                "You must be a candidate to login this way. Are you an Employer?"
            )


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

        """Initialize the form so it contains the 
            information the user has already provided"""
        
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
