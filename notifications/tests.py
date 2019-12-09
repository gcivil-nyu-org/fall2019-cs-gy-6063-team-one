from django.test import TestCase

from uplyft.tests.decorators import setUpMockedS3
from uplyft.tests.resources import (
    test_user_data,
    create_candidate_with_active_profile,
    create_job,
    create_profile,
    create_department,
    create_employer,
)


@setUpMockedS3
class NotificationCenterTests(TestCase):
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

    def setUp(self):
        self.candidate = create_candidate_with_active_profile(
            test_user_data["candidate"]
        )
        self.department = create_department(test_user_data["department"])
        self.employer = create_employer(self.department, test_user_data["employer"])
        self.job = create_job(self.department, test_user_data["job_details"][0])
        self.profile = create_profile(test_user_data["candidate"]["profile"])

    def test_view_url_exists_at_desired_location_candidate(self):
        self.login_candidate()
        response = self.client.get("/notifications/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_at_desired_location_employer(self):
        self.login_employer()
        response = self.client.get("/notifications/")
        self.assertEqual(response.status_code, 200)
