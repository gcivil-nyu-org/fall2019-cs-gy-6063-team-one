from django.test import TestCase
from django.urls import reverse

from uplyft.tests.resources import (
    test_user_data,
    create_job,
    create_application,
    create_candidate,
    create_department,
    create_employer,
)


class DashboardViewTests(TestCase):
    def setUp(self):
        self.department = create_department(test_user_data["department"])
        self.employer = create_employer(self.department, test_user_data["employer"])
        self.candidate = create_candidate(test_user_data["candidate"])
        self.job = create_job(self.department, test_user_data["job_details"][0])
        self.app = create_application(self.job, self.candidate)

    def login_candidate(self):
        self.client.login(
            email=test_user_data["candidate"]["email"],
            password=test_user_data["candidate"]["password"],
        )

    def login_employer(self):
        self.client.login(
            email=test_user_data["employer"]["email"],
            password=test_user_data["employer"]["password"],
        )

    def test_view_url_stays_if_no_login(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)

    def test_view_template_if_no_login(self):
        response = self.client.get("")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "uplyft/base.html")
        self.assertTemplateUsed(response, "uplyft/index.html")

    def test_view_url_redirects_candidate(self):
        self.login_candidate()
        response = self.client.get("")
        self.assertEqual(response.status_code, 302)

    def test_view_url_redirects_employer(self):
        self.login_employer()
        response = self.client.get("")
        self.assertEqual(response.status_code, 302)

    def test_view_url_is_accessible_by_name_candidate(self):
        self.login_candidate()
        response = self.client.get(reverse("uplyft:index"))
        self.assertEqual(response.status_code, 302)

    def test_view_url_is_accessible_by_name_employer(self):
        self.login_employer()
        response = self.client.get(reverse("uplyft:index"))
        self.assertEqual(response.status_code, 302)
