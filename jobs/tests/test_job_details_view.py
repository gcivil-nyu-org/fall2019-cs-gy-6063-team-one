from django.test import TestCase
from django.urls import reverse
from uplyft.tests.resources import (
    create_department,
    create_job,
    create_application,
    create_candidate_with_active_profile,
    create_employer,
    test_user_data,
    create_profile,
)
from uplyft.tests.decorators import setUpMockedS3


@setUpMockedS3
class JobDetailViewTests(TestCase):
    def login_candidate(self):
        self.client.login(
            email=test_user_data["candidate"]["email"],
            password=test_user_data["candidate"]["password"],
        )

    def setUp(self):
        self.candidate = create_candidate_with_active_profile(
            test_user_data["candidate"]
        )
        self.department = create_department(test_user_data["department"])
        self.employer = create_employer(self.department, test_user_data["employer"])
        self.job = create_job(self.department, test_user_data["job_details"][0])
        self.profile = create_profile(test_user_data["candidate"]["profile"])
        self.app = create_application(self.job, self.candidate, self.profile)

    def test_view_url_accessible_by_name_and_pk(self):
        self.login_candidate()
        response = self.client.get(
            reverse("jobs:job_detail", kwargs={"pk": self.job.id})
        )
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.login_candidate()
        response = self.client.get(
            reverse("jobs:job_detail", kwargs={"pk": self.job.id})
        )
        self.assertTemplateUsed(response, "uplyft/base.html")
        self.assertTemplateUsed(response, "jobs/job_detail.html")

    def test_view_returns_job_details(self):
        self.login_candidate()
        response = self.client.get(
            reverse("jobs:job_detail", kwargs={"pk": self.job.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.job.business_title)

    def test_view_returns_job_context(self):
        self.login_candidate()
        response = self.client.get(
            reverse("jobs:job_detail", kwargs={"pk": self.job.id})
        )
        self.assertEqual(response.status_code, 200)
