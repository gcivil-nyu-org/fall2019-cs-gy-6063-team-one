from django.forms import ModelForm, BooleanField
from uplyft.models import CandidateProfile, ActiveProfile


class ApplicationForm(ModelForm):
    # Check box for whether the user wants to push changes to their profile
    update_profile = BooleanField(initial=False, required=False)

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
            "update_profile",
        )

    def __init__(self, *args, **kwargs):
        candidate = kwargs.pop("instance")
        active_prof = ActiveProfile.objects.get(candidate=candidate)
        super(ApplicationForm, self).__init__(*args, **kwargs)
        """
        Initialize the form so it contains the
        information the user has already provided
        """

        # Set some of the fields to be required
        self.fields["first_name"].required = True
        self.fields["last_name"].required = True
        self.fields["address_line"].required = True
        self.fields["zip_code"].required = True
        self.fields["state"].required = True
        self.fields["email"].required = True

        self.fields["phone"].required = True
        self.fields["education"].required = True
        self.fields["experiences"].required = True
        self.fields["cover_letter"].required = True

        # Make sure the first letter of the user's first and last name are capitalize
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
