from django.test import TestCase

from register.forms import EmployerRegistrationForm
from uplyft.tests.resources import (
    test_user_data,
    create_candidate_with_active_profile,
    create_job,
    create_profile,
    create_department,
    create_employer,
)


class EmployerRegistrationFormTests(TestCase):
    def setUp(self):
        self.candidate = create_candidate_with_active_profile(
            test_user_data["candidate"]
        )
        self.department = create_department(test_user_data["department"])
        self.employer = create_employer(self.department, test_user_data["employer"])
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

    # def test_department_field_label(self):
    #     form = EmployerRegistrationForm()
    #     self.assertTrue(form.fields["department"].label == "Department")

    def test_missing_department_form_invalid(self):
        form = EmployerRegistrationForm(data=test_user_data["employer"])
        self.assertFalse(form.is_valid())

    # def test_all_good_form_valid(self):
    #     form = EmployerRegistrationForm(
    #         data={
    #             "first_name": test_user_data["candidate"]["first_name"],
    #             "last_name": test_user_data["candidate"]["last_name"],
    #             "email": test_user_data["candidate"]["email"],
    #             "password1": test_user_data["candidate"]["password"],
    #             "password2": test_user_data["candidate"]["password"],
    #             "department": self.job.department,
    #         }
    #     )
    #     self.assertTrue(form.is_valid())
