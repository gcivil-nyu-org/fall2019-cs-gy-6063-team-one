from django.test import TestCase
from django.urls import reverse

from uplyft.tests.decorators import setUpMockedS3
from uplyft.tests.resources import (
    test_user_data,
    create_candidate_with_active_profile,
    create_job,
    create_application,
    create_profile,
    create_department,
    create_employer,
)
from .models import Notification


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
        self.app = create_application(self.job, self.candidate, self.profile)

    def test_view_url_exists_at_desired_location_candidate(self):
        self.login_candidate()
        response = self.client.get("/notifications/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_exists_at_desired_location_employer(self):
        self.login_employer()
        response = self.client.get("/notifications/")
        self.assertEqual(response.status_code, 200)

    def test_NC_application_rejected_notification(self):
        self.login_employer()
        self.client.post(
            reverse("applications:application_details", kwargs={"pk": self.app.id}),
            {"reject_button": "Reject"},
        )
        self.login_candidate()
        notification_center_page = self.client.get(
            reverse("notifications:notification_center")
        )
        self.assertEqual(len(notification_center_page.context["entities"].keys()), 1)

    # TODO: test NC handling of other notification entities or types

    def test_NC_read_all(self):
        self.login_employer()
        self.client.post(
            reverse("applications:application_details", kwargs={"pk": self.app.id}),
            {"reject_button": "Reject"},
        )
        self.login_candidate()
        notification_center_page = self.client.get(
            reverse("notifications:notification_center")
        )
        user = notification_center_page.context["user"]
        unreadNotifications = Notification.objects.filter(
            recipient=user, status=Notification.STATUS_UNREAD
        )
        self.assertEqual(unreadNotifications.count(), 1)
        self.client.get(reverse("notifications:readall"))
        unreadNotifications = Notification.objects.filter(
            recipient=user, status=Notification.STATUS_UNREAD
        )
        self.assertEqual(unreadNotifications.count(), 0)
