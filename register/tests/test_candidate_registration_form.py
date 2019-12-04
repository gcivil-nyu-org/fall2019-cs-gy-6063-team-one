from django.contrib.auth import get_user_model
from django.test import TestCase

from register.forms import CandidateRegistrationForm
from uplyft.tests.resources import test_user_data
from uplyft.tests.decorators import setUpMockedS3


@setUpMockedS3
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
        form = CandidateRegistrationForm(data=test_user_data["candidate"])
        self.assertTrue(form.is_valid())

    def test_first_name_missing(self):
        form = CandidateRegistrationForm(
            data={
                "first_name": "",
                "last_name": test_user_data["candidate"]["last_name"],
                "email": test_user_data["candidate"]["email"],
                "password1": test_user_data["candidate"]["password"],
                "password2": test_user_data["candidate"]["password"],
            }
        )
        self.assertFalse(form.is_valid())

    def test_last_name_missing(self):
        form = CandidateRegistrationForm(
            data={
                "first_name": test_user_data["candidate"]["first_name"],
                "last_name": "",
                "email": test_user_data["candidate"]["email"],
                "password1": test_user_data["candidate"]["password"],
                "password2": test_user_data["candidate"]["password"],
            }
        )
        self.assertFalse(form.is_valid())

    def test_email_missing(self):
        form = CandidateRegistrationForm(
            data={
                "first_name": test_user_data["candidate"]["first_name"],
                "last_name": test_user_data["candidate"]["last_name"],
                "email": "",
                "password1": test_user_data["candidate"]["password"],
                "password2": test_user_data["candidate"]["password"],
            }
        )
        self.assertFalse(form.is_valid())

    def test_password1_missing(self):
        form = CandidateRegistrationForm(
            data={
                "first_name": test_user_data["candidate"]["first_name"],
                "last_name": test_user_data["candidate"]["last_name"],
                "email": test_user_data["candidate"]["email"],
                "password1": "",
                "password2": test_user_data["candidate"]["password"],
            }
        )
        self.assertFalse(form.is_valid())

    def test_password2_missing(self):
        form = CandidateRegistrationForm(
            data={
                "first_name": test_user_data["candidate"]["first_name"],
                "last_name": test_user_data["candidate"]["last_name"],
                "email": test_user_data["candidate"]["email"],
                "password1": test_user_data["candidate"]["password"],
                "password2": "",
            }
        )
        self.assertFalse(form.is_valid())

    def test_password2_mismatch(self):
        form = CandidateRegistrationForm(
            data={
                "first_name": test_user_data["candidate"]["first_name"],
                "last_name": test_user_data["candidate"]["last_name"],
                "email": test_user_data["candidate"]["email"],
                "password1": test_user_data["candidate"]["password"],
                "password2": test_user_data["employer"]["password"],
            }
        )
        self.assertFalse(form.is_valid())

    def test_first_name_invalid(self):
        form = CandidateRegistrationForm(
            data={
                "first_name": test_user_data["invalid_user_details"]["first_name"],
                "last_name": test_user_data["candidate"]["last_name"],
                "email": test_user_data["candidate"]["email"],
                "password1": test_user_data["candidate"]["password"],
                "password2": test_user_data["candidate"]["password"],
            }
        )
        self.assertFalse(form.is_valid())

    def test_last_name_invalid(self):
        form = CandidateRegistrationForm(
            data={
                "first_name": test_user_data["candidate"]["first_name"],
                "last_name": test_user_data["invalid_user_details"]["last_name"],
                "email": test_user_data["candidate"]["email"],
                "password1": test_user_data["candidate"]["password"],
                "password2": test_user_data["candidate"]["password"],
            }
        )
        self.assertFalse(form.is_valid())

    def test_email_invalid(self):
        form = CandidateRegistrationForm(
            data={
                "first_name": test_user_data["candidate"]["first_name"],
                "last_name": test_user_data["candidate"]["last_name"],
                "email": test_user_data["invalid_user_details"]["email"],
                "password1": test_user_data["candidate"]["password"],
                "password2": test_user_data["candidate"]["password"],
            }
        )
        self.assertFalse(form.is_valid())

    def test_email_taken(self):
        get_user_model().objects.create(
            first_name=test_user_data["candidate"]["first_name"],
            last_name=test_user_data["candidate"]["last_name"],
            email=test_user_data["candidate"]["email"],
            password=test_user_data["candidate"]["password"],
        )
        form = CandidateRegistrationForm(
            data={
                "first_name": test_user_data["candidate"]["first_name"],
                "last_name": test_user_data["candidate"]["last_name"],
                "email": test_user_data["candidate"]["email"],
                "password1": test_user_data["candidate"]["password"],
                "password2": test_user_data["candidate"]["password"],
            }
        )
        self.assertFalse(form.is_valid())
