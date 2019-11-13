from django.contrib.auth import authenticate
from django.test import TestCase
from django.urls import reverse

from employer_login.forms import EmployerLoginForm
from uplyft.tests.resources import (
    test_user_data,
    create_department,
    create_user,
    create_employer,
)

login_url = "/employer_login/"


class LoginWithStandardAuthTestCase(TestCase):
    def setUp(self):
        self.department = create_department(test_user_data["department"])
        self.employer = create_employer(self.department, test_user_data["employer"])
        self.user = self.employer.user
        self.inactive_user = create_user(test_user_data["candidate"], False, False)

    def test_employer_login(self):
        response = self.client.post(
            reverse("employer_login:employer_login"),
            data={"username": self.user.email, "password": self.user.password},
        )
        print("self.user.email: " + self.user.email)
        print("self.user.pw: " + self.user.password)
        self.assertEquals(response.status_code, 200)
        print(response.content)
        self.assertContains(response, "Dashboard")

    def test_inactive_user_login(self):
        response = self.client.post(
            reverse("employer_login:employer_login"),
            data={
                "username": self.inactive_user.email,
                "password": self.inactive_user.password,
            },
        )
        # print(response.content)
        self.assertNotEquals(response.status_code, 200)

    def test_user_authenticate_wrong_password(self):
        authenticated_user = authenticate(
            email=test_user_data["employer"]["email"],
            password=test_user_data["employer"]["password"]
            + test_user_data["employer"]["password"],
        )
        self.assertIsNone(authenticated_user)

    def test_user_authenticate_invalid_user(self):
        authenticated_user = authenticate(
            email=test_user_data["employer"]["first_name"],
            password=test_user_data["employer"]["password"],
        )
        self.assertIsNone(authenticated_user)

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(login_url)
        self.assertEqual(response.status_code, 200)

    def test_view_url_is_accessible_by_name(self):
        response = self.client.get(reverse("employer_login:employer_login"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("employer_login:employer_login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "uplyft/base.html")
        self.assertTemplateUsed(response, "employer_login/employer_login.html")

    def test_form_passed_in_context(self):
        response = self.client.get(reverse("employer_login:employer_login"))
        self.assertTrue("form" in response.context)
        self.assertIsInstance(response.context["form"], EmployerLoginForm)


#     def test_login_with_correct_credentials(self):
#         client = Client()
#         can_login = client.login(
#             username=test_user_data["employer"]["email"],
#             password=test_user_data["employer"]["password"]
#         )
#         self.assertTrue(can_login)
#
#     def test_login_with_incorrect_credentials(self):
#         client = Client()
#         can_login = client.login(
#             username=test_user_data["employer"]["email"],
#             password=
#             test_user_data["employer"]["password"] +
#             test_user_data["employer"]["password"]
#         )
#         self.assertFalse(can_login)
#
#
# class PostLoginWithStandardAuthTestCase(TestCase):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.client = Client()
#
#     def setUp(self):
#         self.user = create_user(test_user_data["employer"], False)
#
#     def test_user_access_user_profile(self):
#         self.client.login(username=test_user_data["employer"]["email"],
#                           password=test_user_data["employer"]["password"])
#         response = self.client.get("/employer_login/success/")
#         self.assertRedirects(
#             response, reverse("jobs:jobs"), fetch_redirect_response=False
#         )
