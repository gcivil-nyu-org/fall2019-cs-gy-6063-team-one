from django.test import TestCase
from django.urls import reverse
from register.forms import EmployerRegistrationForm
from uplyft.tests.resources import (
    test_user_data,
    create_candidate_with_active_profile,
    create_job,
    create_profile,
    create_department,
    create_employer,
)
from uplyft.tests.decorators import setUpMockedS3
from uplyft.models import Employer


@setUpMockedS3
class EmployerRegistrationFormTests(TestCase):
    def setUp(self):
        self.candidate = create_candidate_with_active_profile(
            test_user_data["candidate"]
        )
        self.department = create_department(test_user_data["department"])
        self.job = create_job(self.department, test_user_data["job_details"][0])
        self.profile = create_profile(test_user_data["candidate"]["profile"])

    def test_first_name_field_label(self):
        form = EmployerRegistrationForm()
        self.assertTrue(form.fields["first_name"].label == "First Name")

    def test_last_name_field_label(self):
        form = EmployerRegistrationForm()
        self.assertTrue(form.fields["last_name"].label == "Last Name")

    def test_email_field_label(self):
        form = EmployerRegistrationForm()
        self.assertTrue(form.fields["email"].label == "Email")

    def test_department_field_label(self):
        form = EmployerRegistrationForm()
        self.assertTrue(form.fields["department"].label == "Department")

    def test_all_good_form_valid(self):
        form = EmployerRegistrationForm(
            data={
                "first_name": test_user_data["employers"][1]["first_name"],
                "last_name": test_user_data["employers"][1]["last_name"],
                "email": test_user_data["employers"][1]["email"],
                "password1": test_user_data["employers"][1]["password"],
                "password2": test_user_data["employers"][1]["password"],
                "department": self.job.department.id,
            }
        )
        self.assertTrue(form.is_valid())

    def test_missing_department_form_invalid(self):
        form = EmployerRegistrationForm(
            data={
                "first_name": test_user_data["employers"][1]["first_name"],
                "last_name": test_user_data["employers"][1]["last_name"],
                "email": test_user_data["employers"][1]["email"],
                "password1": test_user_data["employers"][1]["password"],
                "password2": test_user_data["employers"][1]["password"],
            }
        )
        self.assertFalse(form.is_valid())

    def test_invalid_first_name_form_invalid(self):
        form = EmployerRegistrationForm(
            data={
                "first_name": test_user_data["invalid_user_details"]["first_name"],
                "last_name": test_user_data["employers"][1]["last_name"],
                "email": test_user_data["employers"][1]["email"],
                "password1": test_user_data["employers"][1]["password"],
                "password2": test_user_data["employers"][1]["password"],
                "department": self.job.department.id,
            }
        )
        self.assertFalse(form.is_valid())

    def test_invalid_last_name_form_invalid(self):
        form = EmployerRegistrationForm(
            data={
                "first_name": test_user_data["employers"][1]["first_name"],
                "last_name": test_user_data["invalid_user_details"]["last_name"],
                "email": test_user_data["employers"][1]["email"],
                "password1": test_user_data["employers"][1]["password"],
                "password2": test_user_data["employers"][1]["password"],
                "department": self.job.department.id,
            }
        )
        self.assertFalse(form.is_valid())

    def test_email_already_taken_form_invalid(self):
        employer = create_employer(self.department, test_user_data["employer"])
        form = EmployerRegistrationForm(
            data={
                "first_name": test_user_data["employers"][1]["first_name"],
                "last_name": test_user_data["employers"][1]["last_name"],
                "email": employer.user.email,
                "password1": test_user_data["employers"][1]["password"],
                "password2": test_user_data["employers"][1]["password"],
                "department": self.job.department.id,
            }
        )
        self.assertFalse(form.is_valid())

    def test_register_post_form_redirects_to_email_confirmation(self):
        response = self.client.post(
            reverse("register:employer_register"),
            data={
                "first_name": test_user_data["employers"][1]["first_name"],
                "last_name": test_user_data["employers"][1]["last_name"],
                "email": test_user_data["employers"][1]["email"],
                "password1": test_user_data["employers"][1]["password"],
                "password2": test_user_data["employers"][1]["password"],
                "department": self.job.department.id,
            },
        )
        self.assertRedirects(
            response,
            reverse("register:email_confirmation"),
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )

    def test_register_post_form_creates_inactive_employer(self):
        self.client.post(
            reverse("register:employer_register"),
            data={
                "first_name": test_user_data["employers"][1]["first_name"],
                "last_name": test_user_data["employers"][1]["last_name"],
                "email": test_user_data["employers"][1]["email"],
                "password1": test_user_data["employers"][1]["password"],
                "password2": test_user_data["employers"][1]["password"],
                "department": self.job.department.id,
            },
        )
        self.assertEquals(Employer.objects.all().count(), 1)
        employer = Employer.objects.get(id=1)
        self.assertFalse(employer.user.is_active)

    def test_register_bad_post_retains_errors(self):
        response = self.client.post(
            reverse("register:employer_register"),
            data={
                "first_name": test_user_data["employers"][1]["first_name"],
                "last_name": test_user_data["employers"][1]["last_name"],
                "email": test_user_data["employers"][1]["email"],
                "password1": test_user_data["employers"][1]["password"],
                "password2": test_user_data["employers"][1]["password"],
                "department": self.job.department.id,
            },
        )
        self.assertRedirects(
            response,
            reverse("register:email_confirmation"),
            status_code=302,
            target_status_code=200,
            fetch_redirect_response=True,
        )
