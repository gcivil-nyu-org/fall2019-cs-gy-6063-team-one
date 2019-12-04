from django.test import TestCase
from django.urls import reverse
from uplyft.tests.resources import (
    test_user_data,
    create_job,
    create_application,
    create_candidate_with_active_profile,
    create_department,
    create_employer,
    create_profile,
)
from uplyft.tests.decorators import setUpMockedS3


@setUpMockedS3
class DashboardViewTests(TestCase):
    def setUp(self):
        self.department = create_department(test_user_data["department"])
        self.employer = create_employer(self.department, test_user_data["employer"])
        self.candidate = create_candidate_with_active_profile(
            test_user_data["candidate"]
        )
        self.job = create_job(self.department, test_user_data["job_details"][0])
        self.profile = create_profile(test_user_data["candidate"]["profile"])
        self.app = create_application(self.job, self.candidate, self.profile)

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

    def test_view_url_redirects_if_no_login(self):
        response = self.client.get("/dashboard/")
        self.assertEqual(response.status_code, 302)

    def test_view_url_exists_at_desired_location_candidate(self):
        self.login_candidate()
        response = self.client.get("/dashboard/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_at_desired_location_employer(self):
        self.login_employer()
        response = self.client.get("/dashboard/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_is_accessible_by_name_candidate(self):
        self.login_candidate()
        response = self.client.get(reverse("dashboard:dashboard"))
        self.assertEqual(response.status_code, 200)

    def test_view_url_is_accessible_by_name_employer(self):
        self.login_employer()
        response = self.client.get(reverse("dashboard:dashboard"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template_candidate(self):
        self.login_candidate()
        response = self.client.get(reverse("dashboard:dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/dashboard.html")
        self.assertTemplateUsed(response, "dashboard/candidate_dashboard.html")

    def test_view_uses_correct_template_employer(self):
        self.login_employer()
        response = self.client.get(reverse("dashboard:dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/dashboard.html")
        self.assertTemplateUsed(response, "dashboard/employer_dashboard.html")

    def test_view_candidate_shows_pending(self):
        self.login_candidate()
        response = self.client.get(reverse("dashboard:dashboard"))
        self.assertEqual(response.context["pending_count"], 1)

    def test_view_employer_shows_pending(self):
        self.login_employer()
        response = self.client.get(reverse("dashboard:dashboard"))
        self.assertEqual(response.context["pending_count"], 1)

    def test_get_app_first_name_returns_application(self):
        self.login_employer()
        response = self.client.get(
            reverse("dashboard:dashboard", kwargs={"app_status": "ap"}),
            data={"q": f"{self.profile.first_name}"},
        )
        self.assertContains(response, self.profile.first_name)
        self.assertContains(response, self.profile.last_name)
        self.assertContains(response, self.app.id)
        self.assertContains(response, self.app.job.business_title)
        self.assertEqual(response.status_code, 200)

    def test_get_app_last_name_returns_application_card(self):
        self.login_employer()
        response = self.client.get(
            reverse("dashboard:dashboard", kwargs={"app_status": "ap"}),
            data={"q": f"{self.profile.last_name}"},
        )
        self.assertContains(response, self.profile.first_name)
        self.assertContains(response, self.profile.last_name)
        self.assertContains(response, self.app.id)
        self.assertContains(response, self.app.job.business_title)
        self.assertEqual(response.status_code, 200)

    def test_get_app_business_title_returns_application_card(self):
        self.login_employer()
        response = self.client.get(
            reverse("dashboard:dashboard", kwargs={"app_status": "ap"}),
            data={"q": f"{self.job.business_title}"},
        )
        self.assertContains(response, self.profile.first_name)
        self.assertContains(response, self.profile.last_name)
        self.assertContains(response, self.app.id)
        self.assertContains(response, self.app.job.business_title)
        self.assertEqual(response.status_code, 200)

    def test_get_app_first_name_returns_application_candidate(self):
        self.login_candidate()
        response = self.client.get(
            reverse("dashboard:dashboard", kwargs={"app_status": "ap"}),
            data={"q": f"{self.profile.first_name}"},
        )
        self.assertContains(response, self.profile.first_name)
        self.assertContains(response, self.profile.last_name)
        self.assertContains(response, self.app.id)
        self.assertContains(response, self.app.job.business_title)
        self.assertEqual(response.status_code, 200)

    def test_get_app_last_name_returns_application_card_candidate(self):
        self.login_candidate()
        response = self.client.get(
            reverse("dashboard:dashboard", kwargs={"app_status": "ap"}),
            data={"q": f"{self.profile.last_name}"},
        )
        self.assertContains(response, self.profile.first_name)
        self.assertContains(response, self.profile.last_name)
        self.assertContains(response, self.app.id)
        self.assertContains(response, self.app.job.business_title)
        self.assertEqual(response.status_code, 200)

    def test_get_app_business_title_returns_application_card_candidate(self):
        self.login_candidate()
        response = self.client.get(
            reverse("dashboard:dashboard", kwargs={"app_status": "ap"}),
            data={"q": f"{self.job.business_title}"},
        )
        self.assertContains(response, self.profile.first_name)
        self.assertContains(response, self.profile.last_name)
        self.assertContains(response, self.app.id)
        self.assertContains(response, self.app.job.business_title)
        self.assertEqual(response.status_code, 200)
