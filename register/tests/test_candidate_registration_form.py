from django.contrib.auth import get_user_model
from django.test import TestCase

from register.forms import CandidateRegistrationForm
from uplyft.tests.resources import candidate_registration_form_data as data


class CandidateRegistrationFormTests(TestCase):

    def test_first_name_field_label(self):
        form = CandidateRegistrationForm()
        self.assertTrue(form.fields["first_name"].label == "First Name")

    def test_last_name_field_label(self):
        form = CandidateRegistrationForm()
        self.assertTrue(form.fields["last_name"].label == "Last Name")

    def test_email_field_label(self):
        form = CandidateRegistrationForm()
        self.assertTrue(form.fields["email"].label == "Email")

    def test_everything_correct(self):
        form = CandidateRegistrationForm(
            data=data.valid.user1
        )
        self.assertTrue(form.is_valid())

    def test_first_name_missing(self):
        form = CandidateRegistrationForm(
            data=data.invalid.missing_first_name
        )
        self.assertFalse(form.is_valid())

    def test_last_name_missing(self):
        form = CandidateRegistrationForm(
            data=data.invalid.missing_last_name
        )
        self.assertFalse(form.is_valid())

    def test_email_missing(self):
        form = CandidateRegistrationForm(
            data=data.invalid.missing_email
        )
        self.assertFalse(form.is_valid())

    def test_password1_missing(self):
        form = CandidateRegistrationForm(
            data=data.invalid.missing_password1
        )
        self.assertFalse(form.is_valid())

    def test_password2_missing(self):
        form = CandidateRegistrationForm(
            data=data.invalid.missing_password2
        )
        self.assertFalse(form.is_valid())

    def test_password2_mismatch(self):
        form = CandidateRegistrationForm(
            data=data.invalid.password_mismatch
        )
        self.assertFalse(form.is_valid())

    def test_first_name_invalid(self):
        form = CandidateRegistrationForm(
            data=data.invalid.first_name_invalid
        )
        self.assertFalse(form.is_valid())

    def test_last_name_invalid(self):
        form = CandidateRegistrationForm(
            data=data.invalid.last_name_invalid
        )
        self.assertFalse(form.is_valid())

    def test_email_invalid(self):
        form = CandidateRegistrationForm(
            data=data.invalid.email_invalid
        )
        self.assertFalse(form.is_valid())

    def test_email_taken(self):
        get_user_model().objects.create(
            first_name=data.valid.user1.first_name,
            last_name=data.valid.user1.last_name,
            email=data.valid.user1.email,
            password=data.valid.user1.password1,
        )
        form = CandidateRegistrationForm(
            data=data.valid.user1
        )
        self.assertFalse(form.is_valid())
