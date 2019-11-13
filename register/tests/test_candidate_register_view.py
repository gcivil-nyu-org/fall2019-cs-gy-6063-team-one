from django.test import TestCase
from django.urls import reverse
from django.utils.html import escape

from register.forms import CandidateRegistrationForm
from uplyft.models import CustomUser
from uplyft.tests.resources import test_user_data


class CandidateRegisterViewTests(TestCase):
    def good_POST(self):
        return self.client.post(
            reverse("register:candidate_register"),
            data={
                "first_name": test_user_data["candidate"]["first_name"],
                "last_name": test_user_data["candidate"]["last_name"],
                "email": test_user_data["candidate"]["email"],
                "password1": test_user_data["candidate"]["password"],
                "password2": test_user_data["candidate"]["password"],
            },
        )

    def bad_POST_first_name(self):
        return self.client.post(
            reverse("register:candidate_register"),
            data={
                "first_name": test_user_data["invalid_user_details"]["first_name"],
                "last_name": test_user_data["candidate"]["last_name"],
                "email": test_user_data["candidate"]["email"],
                "password1": test_user_data["candidate"]["password"],
                "password2": test_user_data["candidate"]["password"],
            },
        )

    def bad_POST_last_name(self):
        return self.client.post(
            reverse("register:candidate_register"),
            data={
                "first_name": test_user_data["candidate"]["first_name"],
                "last_name": test_user_data["invalid_user_details"]["last_name"],
                "email": test_user_data["candidate"]["email"],
                "password1": test_user_data["candidate"]["password"],
                "password2": test_user_data["candidate"]["password"],
            },
        )

    def bad_POST_email(self):
        return self.client.post(
            reverse("register:candidate_register"),
            data={
                "first_name": test_user_data["candidate"]["first_name"],
                "last_name": test_user_data["candidate"]["last_name"],
                "email": test_user_data["invalid_user_details"]["email"],
                "password1": test_user_data["candidate"]["password"],
                "password2": test_user_data["candidate"]["password"],
            },
        )

    def bad_POST_password_invalid(self):
        return self.client.post(
            reverse("register:candidate_register"),
            data={
                "first_name": test_user_data["candidate"]["first_name"],
                "last_name": test_user_data["candidate"]["last_name"],
                "email": test_user_data["candidate"]["email"],
                "password1": test_user_data["invalid_user_details"]["password"],
                "password2": test_user_data["invalid_user_details"]["password"],
            },
        )

    def bad_POST_password_mismatch(self):
        return self.client.post(
            reverse("register:candidate_register"),
            data={
                "first_name": test_user_data["candidate"]["first_name"],
                "last_name": test_user_data["candidate"]["last_name"],
                "email": test_user_data["candidate"]["email"],
                "password1": test_user_data["candidate"]["password"],
                "password2": test_user_data["employer"]["password"],
            },
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/register/candidate_register")
        self.assertEqual(response.status_code, 200)

    def test_view_url_is_accessible_by_name(self):
        response = self.client.get(reverse("register:candidate_register"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("register:candidate_register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "uplyft/base.html")
        self.assertTemplateUsed(response, "register/candidate_register.html")

    def test_form_passed_in_context(self):
        response = self.client.get(reverse("register:candidate_register"))
        self.assertTrue("form" in response.context)
        self.assertIsInstance(response.context["form"], CandidateRegistrationForm)

    def test_good_POST_creates_new_user(self):
        self.good_POST()
        self.assertEqual(CustomUser.objects.count(), 1)

    def test_good_POST_creates_new_user_with_correct_details(self):
        self.good_POST()
        new_user = CustomUser.objects.first()
        self.assertEqual(
            new_user.first_name, test_user_data["candidate"]["first_name"].lower()
        )
        self.assertEqual(
            new_user.last_name, test_user_data["candidate"]["last_name"].lower()
        )
        self.assertEqual(new_user.email, test_user_data["candidate"]["email"].lower())
        self.assertTrue(
            new_user.check_password(test_user_data["candidate"]["password"])
        )

    def test_good_POST_redirects_to_login_success(self):
        response = self.good_POST()
        self.assertRedirects(
            response,
            reverse("candidate_login:candidate_login"),
            fetch_redirect_response=False,
        )

    def test_good_POST_success_message_added_to_context_of_login_success_page(self):
        response = self.client.post(
            reverse("register:candidate_register"),
            data={
                "first_name": test_user_data["candidate"]["first_name"],
                "last_name": test_user_data["candidate"]["last_name"],
                "email": test_user_data["candidate"]["email"],
                "password1": test_user_data["candidate"]["password"],
                "password2": test_user_data["candidate"]["password"],
            },
            follow=True,
        )
        messages = list(response.context["messages"])
        self.assertEqual(str(messages[0]), "Account created successfully")

    def test_bad_POST_first_name_retains_form_data(self):
        response = self.bad_POST_first_name()
        self.assertContains(
            response, test_user_data["invalid_user_details"]["first_name"]
        )
        self.assertContains(response, test_user_data["candidate"]["last_name"])
        self.assertContains(response, test_user_data["candidate"]["email"])

    def test_bad_POST_last_name_retains_form_data(self):
        response = self.bad_POST_last_name()
        self.assertContains(response, test_user_data["candidate"]["first_name"])
        self.assertContains(response, test_user_data["candidate"]["email"])
        self.assertContains(
            response, test_user_data["invalid_user_details"]["last_name"]
        )

    def test_bad_POST_email_retains_form_data(self):
        response = self.bad_POST_email()
        self.assertContains(response, test_user_data["candidate"]["first_name"])
        self.assertContains(response, test_user_data["candidate"]["last_name"])
        self.assertContains(response, test_user_data["invalid_user_details"]["email"])

    def test_bad_POST_password_numeric_retains_form_data(self):
        response = self.bad_POST_password_invalid()
        self.assertContains(response, test_user_data["candidate"]["first_name"])
        self.assertContains(response, test_user_data["candidate"]["last_name"])
        self.assertContains(response, test_user_data["candidate"]["email"])

    def test_bad_POST_password_mismatch_retains_form_data(self):
        response = self.bad_POST_password_mismatch()
        self.assertContains(response, test_user_data["candidate"]["first_name"])
        self.assertContains(response, test_user_data["candidate"]["last_name"])
        self.assertContains(response, test_user_data["candidate"]["email"])

    def test_bad_POST_email_taken_retains_form_data(self):
        CustomUser.objects.create_user(
            first_name=test_user_data["candidate"]["first_name"],
            last_name=test_user_data["candidate"]["last_name"],
            email=test_user_data["candidate"]["email"],
            password=test_user_data["candidate"]["password"],
        )
        response = self.good_POST()
        self.assertContains(response, test_user_data["candidate"]["first_name"])
        self.assertContains(response, test_user_data["candidate"]["last_name"])
        self.assertContains(response, test_user_data["candidate"]["email"])

    def test_bad_POST_first_name_displays_error_message(self):
        response = self.bad_POST_first_name()
        expected_error = "First name should contain only letters (A-Z)."
        self.assertContains(response, escape(expected_error))

    def test_bad_POST_last_name_displays_error_message(self):
        response = self.bad_POST_last_name()
        expected_error = "Last name should contain only letters (A-Z)."
        self.assertContains(response, escape(expected_error))

    def test_bad_POST_email_displays_error_message(self):
        response = self.bad_POST_email()
        expected_error = "Enter a valid email address"
        self.assertContains(response, escape(expected_error))

    def test_bad_POST_password_numeric_displays_error_message(self):
        response = self.bad_POST_password_invalid()
        expected_error = "This password is entirely numeric."
        self.assertContains(response, escape(expected_error))

    def test_bad_POST_password_mismatch_displays_error_message(self):
        response = self.bad_POST_password_mismatch()
        expected_error = "The two password fields didn't match."
        self.assertContains(response, escape(expected_error))

    def test_bad_POST_email_taken_displays_error_message(self):
        CustomUser.objects.create_user(
            first_name=test_user_data["candidate"]["first_name"],
            last_name=test_user_data["candidate"]["last_name"],
            email=test_user_data["candidate"]["email"],
            password=test_user_data["candidate"]["password"],
        )
        response = self.good_POST()
        expected_error = "Email already exists"
        self.assertContains(response, escape(expected_error))

    def test_bad_POST_first_name_correct_template_returned(self):
        response = self.bad_POST_first_name()
        self.assertEqual(response.status_code, 200)

    def test_bad_POST_last_name_correct_template_returned(self):
        response = self.bad_POST_last_name()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register/candidate_register.html")

    def test_bad_POST_email_correct_template_returned(self):
        response = self.bad_POST_email()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register/candidate_register.html")

    def test_bad_POST_password_numeric_correct_template_returned(self):
        response = self.bad_POST_password_invalid()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register/candidate_register.html")

    def test_bad_POST_password_mismatch_correct_template_returned(self):
        response = self.bad_POST_password_mismatch()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register/candidate_register.html")

    def test_bad_POST_email_taken_correct_template_returned(self):
        CustomUser.objects.create_user(
            first_name=test_user_data["candidate"]["first_name"],
            last_name=test_user_data["candidate"]["last_name"],
            email=test_user_data["candidate"]["email"],
            password=test_user_data["candidate"]["password"],
        )
        response = self.good_POST()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register/candidate_register.html")
