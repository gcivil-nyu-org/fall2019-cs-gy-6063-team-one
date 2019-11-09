from django.test import TestCase
from django.urls import reverse
from django.utils.html import escape

from register.forms import CandidateRegistrationForm
from uplyft.models import CustomUser

from uplyft.tests.resources import post_to_view
from uplyft.tests.resources import candidate_registration_form_data as data


class CandidateRegisterViewTests(TestCase):

    def good_POST(self):
        return post_to_view(self, "register:candidate_register",
                            data.valid.user1)

    def bad_POST_first_name_invalid(self):
        return post_to_view(self, view="register:candidate_register",
                            data=data.invalid.first_name_invalid
                            )

    def bad_POST_last_name_invalid(self):
        return post_to_view(self, view="register:candidate_register",
                            data=data.invalid.last_name_invalid)

    def bad_POST_email_missing(self):
        return post_to_view(self, view="register:candidate_register",
                            data=data.invalid.email_invalid)

    def bad_POST_password1_invalid(self):
        return post_to_view(self, view="register:candidate_register",
                            data=data.invalid.password1_invalid)

    def bad_POST_password2_invalid(self):
        return post_to_view(self, view="register:candidate_register",
                            data=data.invalid.password2_invalid)

    def bad_POST_password_mismatch(self):
        return post_to_view(self, view="register:candidate_register",
                            data=data.invalid.password_mismatch)

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
        self.assertEqual(new_user.first_name, data.valid.user1.first_name)
        self.assertEqual(new_user.last_name, data.valid.user1.last_name)
        self.assertEqual(new_user.email, data.valid.user1.email)
        self.assertTrue(new_user.check_password(data.valid.user1.password1))

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
            data=data.valid.user1,
            follow=True,
        )
        messages = list(response.context["messages"])
        self.assertEqual(str(messages[0]), "Account created successfully")

    def test_bad_POST_first_name_invalid_retains_form_data(self):
        response = self.bad_POST_first_name()
        self.assertContains(response, data.invalid.first_name_invalid.first_name)
        self.assertContains(response, data.invalid.first_name_invalid.last_name)
        self.assertContains(response, data.invalid.first_name_invalid.email)

    def test_bad_POST_last_name_invalid_retains_form_data(self):
        response = self.bad_POST_last_name_missing()
        self.assertContains(response, data.invalid.last_name_invalid.first_name)
        self.assertContains(response, data.invalid.last_name_invalid.last_name)
        self.assertContains(response, data.invalid.last_name_invalid.email)

    def test_bad_POST_email_invalid_retains_form_data(self):
        response = self.bad_POST_email_missing()
        self.assertContains(response, data.invalid.email_invalid.first_name)
        self.assertContains(response, data.invalid.email_invalid.last_name)
        self.assertContains(response, data.invalid.email_invalid.first_name)

    def test_bad_POST_password1_invalid_retains_form_data(self):
        response = self.bad_POST_password1_invalid()
        self.assertContains(response, data.valid.user1.first_name)
        self.assertContains(response, data.valid.user1.last_name)
        self.assertContains(response, data.valid.user1.email)

    def test_bad_POST_password_mismatch_retains_form_data(self):
        response = self.bad_POST_password_mismatch()
        self.assertContains(response, data.valid.user1.first_name)
        self.assertContains(response, data.valid.user1.last_name)
        self.assertContains(response, data.valid.user1.email)

    def test_bad_POST_email_taken_retains_form_data(self):
        CustomUser.objects.create_user(
            first_name=data.valid.user1.first_name,
            last_name=data.valid.user1.last_name,
            email=data.valid.user1.email,
            password=data.valid.user1.password,
        )
        response = self.good_POST()
        self.assertContains(response, data.valid.user1.first_name)
        self.assertContains(response, data.valid.user1.last_name)
        self.assertContains(response, data.valid.user1.email)

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
            first_name=data.valid.user1.first_name,
            last_name=data.valid.user1.last_name,
            email=data.valid.user1.email,
            password=data.valid.user1.password1,
        )
        response = self.good_POST()
        expected_error = "Email already exists"
        self.assertContains(response, escape(expected_error))

    def test_bad_POST_first_name_correct_template_returned(self):
        response = self.bad_POST_first_name_invalid()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register/candidate_register.html")

    def test_bad_POST_last_name_correct_template_returned(self):
        response = self.bad_POST_last_name_invalid()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register/candidate_register.html")

    def test_bad_POST_email_correct_template_returned(self):
        response = self.bad_POST_email_invalid()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register/candidate_register.html")

    def test_bad_POST_password1_invalid_correct_template_returned(self):
        response = self.bad_POST_password1_invalid()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register/candidate_register.html")

    def test_bad_POST_password2_invalid_correct_template_returned(self):
        response = self.bad_POST_password2_invalid()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register/candidate_register.html")

    def test_bad_POST_password_mismatch_correct_template_returned(self):
        response = self.bad_POST_password_mismatch()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register/candidate_register.html")

    def test_bad_POST_email_taken_correct_template_returned(self):
        CustomUser.objects.create_user(
            first_name=data.valid.user1.first_name,
            last_name=data.valid.user1.last_name,
            email=data.valid.user1.email,
            password=data.valid.user1.password,
        )
        response = self.good_POST()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "register/candidate_register.html")
