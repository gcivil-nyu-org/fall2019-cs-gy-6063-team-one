from django.test import TestCase
from candidate_profile.forms import CandidateProfileForm
from uplyft.tests.resources import test_user_data, create_candidate_with_active_profile
from uplyft.tests.decorators import setUpMockedS3


@setUpMockedS3
class CandidateProfileFormTests(TestCase):
    def setUp(self):
        self.candidate = create_candidate_with_active_profile(
            test_user_data["candidate"]
        )

    def test_first_name_field_label(self):
        form = CandidateProfileForm(instance=self.candidate)
        self.assertTrue(form.fields["first_name"].label == "First name")

    def test_last_name_field_label(self):
        form = CandidateProfileForm(instance=self.candidate)
        self.assertTrue(form.fields["last_name"].label == "Last name")

    def test_email_field_label(self):
        form = CandidateProfileForm(instance=self.candidate)
        self.assertTrue(form.fields["email"].label == "Email")

    def test_address_field_label(self):
        form = CandidateProfileForm(instance=self.candidate)
        self.assertTrue(form.fields["address_line"].label == "Address line")

    def test_zip_code_field_label(self):
        form = CandidateProfileForm(instance=self.candidate)
        self.assertTrue(form.fields["zip_code"].label == "Zip code")

    def test_state_field_label(self):
        form = CandidateProfileForm(instance=self.candidate)
        self.assertTrue(form.fields["state"].label == "State")

    def test_phone_field_label(self):
        form = CandidateProfileForm(instance=self.candidate)
        self.assertTrue(form.fields["phone"].label == "Phone")

    def test_portfolio_website_field_label(self):
        form = CandidateProfileForm(instance=self.candidate)
        self.assertTrue(form.fields["portfolio_website"].label == "Portfolio website")

    def test_resume_field_label(self):
        form = CandidateProfileForm(instance=self.candidate)
        self.assertTrue(form.fields["resume"].label == "Resume")

    def test_gender_label(self):
        form = CandidateProfileForm(instance=self.candidate)
        self.assertTrue(form.fields["gender"].label == "Gender")

    def test_ethnicity_label(self):
        form = CandidateProfileForm(instance=self.candidate)
        self.assertTrue(form.fields["ethnicity"].label == "Ethnicity")

    def test_race_label(self):
        form = CandidateProfileForm(instance=self.candidate)
        self.assertTrue(form.fields["race"].label == "Race")

    def test_health_conditions_label(self):
        form = CandidateProfileForm(instance=self.candidate)
        self.assertTrue(form.fields["health_conditions"].label == "Health conditions")

    def test_veteran_label(self):
        form = CandidateProfileForm(instance=self.candidate)
        self.assertTrue(form.fields["veteran"].label == "Veteran")

    def test_everything_correct(self):
        form = CandidateProfileForm(
            instance=self.candidate, data=test_user_data["candidate"]["profile"]
        )
        self.assertTrue(form.is_valid())

    # def test_only_first_name_form_still_valid(self):
    #     form = CandidateProfileForm(instance=self.candidate, data={
    #         "first_name": test_user_data["candidate"]["new_profile"]["first_name"],
    #     })
    #     self.assertTrue(form.is_valid())
    #
    # def test_only_last_name_form_still_valid(self):
    #     form = CandidateProfileForm(instance=self.candidate, data={
    #         "last_name": test_user_data["candidate"]["new_profile"]["last_name"],
    #     })
    #     self.assertTrue(form.is_valid())
    #
    # def test_only_address_line_form_still_valid(self):
    #     form = CandidateProfileForm(instance=self.candidate, data={
    #         "address_line":
    #         test_user_data["candidate"]["new_profile"]["address_line"],
    #     })
    #     self.assertTrue(form.is_valid())
    #
    # def test_only_zip_code_form_still_valid(self):
    #     form = CandidateProfileForm(instance=self.candidate, data={
    #         "zip_code": test_user_data["candidate"]["new_profile"]["zip_code"],
    #     })
    #     self.assertTrue(form.is_valid())
    #
    # def test_only_state_form_still_valid(self):
    #     form = CandidateProfileForm(instance=self.candidate, data={
    #         "state": test_user_data["candidate"]["new_profile"]["state"],
    #     })
    #     self.assertTrue(form.is_valid())
    #
    # def test_only_email_form_still_valid(self):
    #     form = CandidateProfileForm(instance=self.candidate, data={
    #         "email": test_user_data["candidate"]["new_profile"]["email"],
    #     })
    #     self.assertTrue(form.is_valid())
    #
    # def test_only_phone_form_still_valid(self):
    #     form = CandidateProfileForm(instance=self.candidate, data={
    #         "phone": test_user_data["candidate"]["new_profile"]["phone"],
    #     })
    #     self.assertTrue(form.is_valid())
    #
    # def test_only_portfolio_website_form_still_valid(self):
    #     form = CandidateProfileForm(instance=self.candidate, data={
    #         "portfolio_website":
    #         test_user_data["candidate"]["new_profile"]["portfolio_website"],
    #     })
    #     self.assertTrue(form.is_valid())
    #
    # def test_only_education_form_still_valid(self):
    #     form = CandidateProfileForm(instance=self.candidate, data={
    #         "education": test_user_data["candidate"]["new_profile"][
    #             "education"],
    #     })
    #     self.assertTrue(form.is_valid())
    #
    # def test_only_experiences_form_still_valid(self):
    #     form = CandidateProfileForm(instance=self.candidate, data={
    #         "experiences": test_user_data["candidate"]["new_profile"][
    #             "experiences"],
    #     })
    #     self.assertTrue(form.is_valid())
    #
    # def test_only_cover_letter_form_still_valid(self):
    #     form = CandidateProfileForm(instance=self.candidate, data={
    #         "cover_letter": test_user_data["candidate"]["new_profile"][
    #             "cover_letter"],
    #     })
    #     self.assertTrue(form.is_valid())
    #
    # def test_only_gender_form_still_valid(self):
    #     form = CandidateProfileForm(instance=self.candidate, data={
    #         "gender": test_user_data["candidate"]["new_profile"][
    #             "gender"],
    #     })
    #     self.assertTrue(form.is_valid())
    #
    # def test_only_ethnicity_form_still_valid(self):
    #     form = CandidateProfileForm(instance=self.candidate, data={
    #         "ethnicity": test_user_data["candidate"]["new_profile"][
    #             "ethnicity"],
    #     })
    #     self.assertTrue(form.is_valid())
    #
    # def test_only_race_form_still_valid(self):
    #     form = CandidateProfileForm(instance=self.candidate, data={
    #         "race": test_user_data["candidate"]["new_profile"][
    #             "race"],
    #     })
    #     self.assertTrue(form.is_valid())
    #
    # def test_only_health_conditions_form_still_valid(self):
    #     form = CandidateProfileForm(instance=self.candidate, data={
    #         "health_conditions": test_user_data["candidate"]["new_profile"][
    #             "health_conditions"],
    #     })
    #     self.assertTrue(form.is_valid())
    #
    # def test_nothing_passed_retains_user_data(self):
    #     form = CandidateProfileForm(instance=self.candidate)
    #     form.is_valid()
    #     self.assertTrue(form.is_valid())
    #
    # def test_only_veteran_form_still_valid(self):
    #     form = CandidateProfileForm(instance=self.candidate, data={
    #         "veteran": test_user_data["candidate"]["new_profile"][
    #             "veteran"],
    #     })
    #     self.assertTrue(form.is_valid())
    #
    # # Failing
    # def test_first_name_invalid(self):
    #     form = CandidateProfileForm(instance=self.candidate, data={
    #         "first_name": test_user_data["invalid_user_details"]["first_name"],
    #     })
    #     self.assertFalse(form.is_valid())
    #
    # def test_last_name_invalid(self):
    #     pass
