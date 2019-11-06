from django.contrib.auth import authenticate
from django.test import TestCase, Client
from django.urls import reverse

from candidate_login.views import CandidateLoginView
from uplyft.models import CustomUser

foo_user = {
    "first_name": "John",
    "last_name": "Johnson",
    "email": "john@example.com",
    "password": "cN3KJXi4GxsCxZET",
}

login_url = "/candidate_login/"


def createFooUser():
    CustomUser.objects.create_user(
        email=foo_user["email"],
        password=foo_user["password"],
        first_name=foo_user["first_name"],
        last_name=foo_user["last_name"],
    )


class LoginWithStandardAuthTestCase(TestCase):
    def setUp(self):
        createFooUser()

    def test_user_authenticate_with_correct_credentials(self):
        fooUser = authenticate(email=foo_user["email"], password=foo_user["password"])
        self.assertIsNotNone(fooUser)

    def test_user_authenticate_wrong_password(self):
        fooUser = authenticate(
            email=foo_user["email"],
            password=foo_user["password"] + foo_user["password"],
        )
        self.assertIsNone(fooUser)

    def test_user_authenticate_invalid_user(self):
        fooUser = authenticate(
            email=foo_user["first_name"], password=foo_user["password"]
        )
        self.assertIsNone(fooUser)

    def test_login_get_page(self):
        client = Client()
        response = client.get(login_url)
        self.assertEqual(response.template_name[0], CandidateLoginView.template_name)

    def test_login_with_correct_credentials(self):
        client = Client()
        can_login = client.login(
            username=foo_user["email"], password=foo_user["password"]
        )
        self.assertTrue(can_login)

    def test_login_with_incorrect_credentials(self):
        client = Client()
        can_login = client.login(
            username=foo_user["email"],
            password=foo_user["password"] + foo_user["password"],
        )
        self.assertFalse(can_login)

    def test_anonymoususer_access_user_profile(self):
        client = Client()
        response = client.get("/candidate_login/success/")
        self.assertEqual(response.status_code, 302)


class PostLoginWithStandardAuthTestCase(TestCase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client = Client()

    def setUp(self):
        createFooUser()
        self.client.login(username=foo_user["email"], password=foo_user["password"])

    def test_user_access_user_profile(self):
        response = self.client.get("/candidate_login/success/")
        self.assertRedirects(
            response, reverse("jobs:jobs"), fetch_redirect_response=False
        )
