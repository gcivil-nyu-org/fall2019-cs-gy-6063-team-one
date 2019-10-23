from django.contrib.auth import get_user_model
from django.test import TestCase

from register.forms import CandidateRegistrationForm
from tests.tests import valid_data, invalid_data


class CandidateRegistrationFormTests(TestCase):
    valid_first_name = "Alex"
    valid_last_name = "Rodriguez"
    valid_email = "username@nyc.gov"
    valid_password = "'LKlk#fvdf94@78!9"
    non_alpha_first_name = "..."
    non_alpha_last_name = "123&&^"
    invalid_email = "response@edu"
    invalid_password = "103348494"

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
            data={
                "first_name": valid_data["first_name"],
                "last_name": valid_data["last_name"],
                "email": valid_data["email"],
                "password1": valid_data["password"],
                "password2": valid_data["password"],
            }
        )
        self.assertTrue(form.is_valid())

    def test_first_name_missing(self):
        form = CandidateRegistrationForm(
            data={
                "first_name": "",
                "last_name": valid_data["last_name"],
                "email": valid_data["email"],
                "password1": valid_data["password"],
                "password2": valid_data["password"],
            }
        )
        self.assertFalse(form.is_valid())

    def test_last_name_missing(self):
        form = CandidateRegistrationForm(
            data={
                "first_name": valid_data["first_name"],
                "last_name": "",
                "email": valid_data["email"],
                "password1": valid_data["password"],
                "password2": valid_data["password"],
            }
        )
        self.assertFalse(form.is_valid())

    def test_email_missing(self):
        form = CandidateRegistrationForm(
            data={
                "first_name": valid_data["first_name"],
                "last_name": valid_data["last_name"],
                "email": "",
                "password1": valid_data["password"],
                "password2": valid_data["password"],
            }
        )
        self.assertFalse(form.is_valid())

    def test_password1_missing(self):
        form = CandidateRegistrationForm(
            data={
                "first_name": valid_data["first_name"],
                "last_name": valid_data["last_name"],
                "email": valid_data["email"],
                "password1": "",
                "password2": valid_data["password"],
            }
        )
        self.assertFalse(form.is_valid())

    def test_password2_missing(self):
        form = CandidateRegistrationForm(
            data={
                "first_name": valid_data["first_name"],
                "last_name": valid_data["last_name"],
                "email": valid_data["email"],
                "password1": valid_data["password"],
                "password2": "",
            }
        )
        self.assertFalse(form.is_valid())

    def test_password2_mismatch(self):
        form = CandidateRegistrationForm(
            data={
                "first_name": valid_data["first_name"],
                "last_name": valid_data["last_name"],
                "email": valid_data["email"],
                "password1": valid_data["password"],
                "password2": invalid_data["password"],
            }
        )
        self.assertFalse(form.is_valid())

    def test_first_name_invalid(self):
        form = CandidateRegistrationForm(
            data={
                "first_name": invalid_data["first_name"],
                "last_name": valid_data["last_name"],
                "email": valid_data["email"],
                "password1": valid_data["password"],
                "password2": valid_data["password"],
            }
        )
        self.assertFalse(form.is_valid())

    def test_last_name_invalid(self):
        form = CandidateRegistrationForm(
            data={
                "first_name": valid_data["first_name"],
                "last_name": invalid_data["last_name"],
                "email": valid_data["email"],
                "password1": valid_data["password"],
                "password2": valid_data["password"],
            }
        )
        self.assertFalse(form.is_valid())

    def test_email_invalid(self):
        form = CandidateRegistrationForm(
            data={
                "first_name": valid_data["first_name"],
                "last_name": valid_data["last_name"],
                "email": invalid_data["email"],
                "password1": valid_data["password"],
                "password2": valid_data["password"],
            }
        )
        self.assertFalse(form.is_valid())

    def test_email_taken(self):
        get_user_model().objects.create(
            first_name=valid_data["first_name"],
            last_name=valid_data["last_name"],
            email=valid_data["email"],
            password=valid_data["password"],
        )
        form = CandidateRegistrationForm(
            data={
                "first_name": valid_data["first_name"],
                "last_name": valid_data["last_name"],
                "email": valid_data["email"],
                "password1": valid_data["password"],
                "password2": valid_data["password"],
            }
        )
        self.assertFalse(form.is_valid())
