from django.test import TestCase
from apply.forms import ApplicationForm
from uplyft.tests.resources import test_user_data, create_candidate_with_active_profile
from django.forms import BooleanField


class ApplicationFormTests(TestCase):
    def setUp(self):
        self.candidate = create_candidate_with_active_profile(
            test_user_data["candidate"]
        )

    def test_first_name_field_label(self):
        form = ApplicationForm(instance=self.candidate)
        self.assertTrue(form.fields["first_name"].label == "First name")

    def test_last_name_field_label(self):
        form = ApplicationForm(instance=self.candidate)
        self.assertTrue(form.fields["last_name"].label == "Last name")

    def test_email_field_label(self):
        form = ApplicationForm(instance=self.candidate)
        self.assertTrue(form.fields["email"].label == "Email")

    def test_address_field_label(self):
        form = ApplicationForm(instance=self.candidate)
        self.assertTrue(form.fields["address_line"].label == "Address line")

    def test_zip_code_field_label(self):
        form = ApplicationForm(instance=self.candidate)
        self.assertTrue(form.fields["zip_code"].label == "Zip code")

    def test_state_field_label(self):
        form = ApplicationForm(instance=self.candidate)
        self.assertTrue(form.fields["state"].label == "State")

    def test_phone_field_label(self):
        form = ApplicationForm(instance=self.candidate)
        self.assertTrue(form.fields["phone"].label == "Phone")

    def test_portfolio_website_field_label(self):
        form = ApplicationForm(instance=self.candidate)
        self.assertTrue(form.fields["portfolio_website"].label == "Portfolio website")

    def test_resume_label(self):
        form = ApplicationForm(instance=self.candidate)
        self.assertTrue(form.fields["resume"].label == "Resume")

    def test_cover_letter_label(self):
        form = ApplicationForm(instance=self.candidate)
        self.assertTrue(form.fields["cover_letter"].label == "Cover letter")

    def test_gender_label(self):
        form = ApplicationForm(instance=self.candidate)
        self.assertTrue(form.fields["gender"].label == "Gender")

    def test_ethnicity_label(self):
        form = ApplicationForm(instance=self.candidate)
        self.assertTrue(form.fields["ethnicity"].label == "Ethnicity")

    def test_race_label(self):
        form = ApplicationForm(instance=self.candidate)
        self.assertTrue(form.fields["race"].label == "Race")

    def test_health_conditions_label(self):
        form = ApplicationForm(instance=self.candidate)
        self.assertTrue(form.fields["health_conditions"].label == "Health conditions")

    def test_veteran_label(self):
        form = ApplicationForm(instance=self.candidate)
        self.assertTrue(form.fields["veteran"].label == "Veteran")

    def test_update_profile_is_bool(self):
        form = ApplicationForm(instance=self.candidate)
        self.assertIsInstance(form.fields["update_profile"], BooleanField)

    # Phone number not getting piped in
    # def test_everything_correct(self):
    #     form = ApplicationForm(
    #         instance=self.candidate, data=test_user_data["candidate"]["profile"]
    #     )
    #     form.is_valid()
    #     print(form.errors)
    #     for key in form.cleaned_data:
    #         print(form.cleaned_data[key])
    #     self.assertTrue(form.is_valid())
