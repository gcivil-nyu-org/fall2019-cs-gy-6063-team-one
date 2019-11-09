from django.test import TestCase
from django.urls import reverse
from django.utils.html import escape

from register.forms import CandidateRegistrationForm
from uplyft.models import CustomUser

from uplyft.tests.resources import POST_to_view, user_data_valid, \
    user_data_invalid, candidate_valid, candidate_invalid_email, \
    candidate_invalid_first_name, \
    candidate_invalid_last_name, candidate_invalid_password1, \
    candidate_invalid_password2, candidate_invalid_password_mismatch

class CandidateRegisterViewTests(TestCase):

    def good_POST(self):
        return POST_to_view(self, "register:candidate_register",
                            candidate_valid)

    def bad_POST_first_name(self):
        return POST_to_view(self, view="register:candidate_register",
                            data=candidate_invalid_first_name)

    def bad_POST_last_name(self):
        return POST_to_view(self, view="register:candidate_register",
                            data=candidate_invalid_last_name)

    def bad_POST_email(self):
        return POST_to_view(self, view="register:candidate_register",
                            data=candidate_invalid_email)

    def bad_POST_password1_invalid(self):
        return POST_to_view(self, view="register:candidate_register",
                                data=candidate_invalid_password1)

    def bad_POST_password2_invalid(self):
        return POST_to_view(self, view="register:candidate_register", data=candidate_invalid_password2)

    def bad_POST_password_mismatch(self):
        return POST_to_view(self, view="register:candidate_register",
                                data=candidate_invalid_password2)

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
        self.assertEqual(new_user.first_name, valid_data["first_name"].lower())
        self.assertEqual(new_user.last_name, valid_data["last_name"].lower())
        self.assertEqual(new_user.email, valid_data["email"].lower())
        self.assertTrue(new_user.check_password(valid_data["password"]))

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
            data=valid_candidate_data,
            follow=True,
        )
        messages = list(response.context["messages"])
        self.assertEqual(str(messages[0]), "Account created successfully")

    def test_bad_POST_first_name_retains_form_data(self):
        response = self.bad_POST_first_name()
        self.assertContains(response, invalid_data["first_name"])
        self.assertContains(response, valid_data["last_name"])
        self.assertContains(response, valid_data["email"])

    def test_bad_POST_last_name_retains_form_data(self):
        response = self.bad_POST_last_name()
        self.assertContains(response, valid_data["first_name"])
        self.assertContains(response, invalid_data["last_name"])
        self.assertContains(response, valid_data["email"])

    def test_bad_POST_email_retains_form_data(self):
        response = self.bad_POST_email()
        self.assertContains(response, valid_data["first_name"])
        self.assertContains(response, valid_data["last_name"])
        self.assertContains(response, invalid_data["email"])

    def test_bad_POST_password_numeric_retains_form_data(self):
        response = self.bad_POST_password_incorrect()
        self.assertContains(response, valid_data["first_name"])
        self.assertContains(response, valid_data["last_name"])
        self.assertContains(response, valid_data["email"])

    def test_bad_POST_password_mismatch_retains_form_data(self):
        response = self.bad_POST_password_mismatch()
        self.assertContains(response, valid_data["first_name"])
        self.assertContains(response, valid_data["last_name"])
        self.assertContains(response, valid_data["email"])

    def test_bad_POST_email_taken_retains_form_data(self):
        CustomUser.objects.create_user(
            first_name=valid_data["first_name"],
            last_name=valid_data["last_name"],
            email=valid_data["email"],
            password=valid_data["password"],
        )
        response = self.good_POST()
        self.assertContains(response, valid_data["first_name"])
        self.assertContains(response, valid_data["last_name"])
        self.assertContains(response, valid_data["email"])

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
        response = self.bad_POST_password_incorrect()
        expected_error = "This password is entirely numeric."
        self.assertContains(response, escape(expected_error))

    def test_bad_POST_password_mismatch_displays_error_message(self):
        response = self.bad_POST_password_mismatch()
        expected_error = "The two password fields didn't match."
        self.assertContains(response, escape(expected_error))

    def test_bad_POST_email_taken_displays_error_message(self):
        CustomUser.objects.create_user(
            first_name=valid_data["first_name"],
            last_name=valid_data["last_name"],
            email=valid_data["email"],
            password=valid_data["password"],
        )
        response = self.good_POST()
        expected_error = "Email already exists"
        self.assertContains(response, escape(expected_error))

    def test_bad_POST_first_name_correct_template_returned(self):
        response = self.bad_POST_first_name()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register/candidate_register.html")

    def test_bad_POST_last_name_correct_template_returned(self):
        response = self.bad_POST_last_name()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register/candidate_register.html")

    def test_bad_POST_email_correct_template_returned(self):
        response = self.bad_POST_email()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register/candidate_register.html")

    def test_bad_POST_password_numeric_correct_template_returned(self):
        response = self.bad_POST_password_incorrect()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register/candidate_register.html")

    def test_bad_POST_password_mismatch_correct_template_returned(self):
        response = self.bad_POST_password_mismatch()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register/candidate_register.html")

    def test_bad_POST_email_taken_correct_template_returned(self):
        CustomUser.objects.create_user(
            first_name=valid_data["first_name"],
            last_name=valid_data["last_name"],
            email=valid_data["email"],
            password=valid_data["password"],
        )
        response = self.good_POST()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register/candidate_register.html")
