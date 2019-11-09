# Create your tests here.
import datetime
from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from uplyft.tests.resources import create_department, create_employer, \
    create_candidate, create_job, create_application, valid_users


class DashboardViewTests(TestCase):
    def setUp(self):
        self.department = create_department()
        self.employer = create_employer(self.department)
        self.candidate = create_candidate()
        self.job = create_job(self.department)
        self.app = create_application(self.job, self.candidate)

    def login_candidate(self):
        self.client.login(
            email=valid_users.candidate1.email,
            password=valid_users.candidate1.password
        )

    def login_employer(self):
        self.client.login(
            email=valid_users.employer1.email, password=valid_users.employer1.password
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
