from django.test import TestCase
from django.urls import reverse
from apply.forms import ApplicationForm
from uplyft.tests.resources import (
    test_user_data,
    create_candidate_with_active_profile,
    create_job,
    create_profile,
    create_department,
    create_employer,
    create_application,
)
from apply.models import Application


class ApplicationViewTests(TestCase):
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
        #self.app = create_application(self.job, self.candidate, self.profile)

    def test_view_url_exists_at_desired_location(self):
        self.login_candidate()
        response = self.client.get(f'/apply/{self.job.id}')
        self.assertEqual(response.status_code, 200)

    def test_view_url_is_accessible_by_name_candidate(self):
        self.login_candidate()
        response = self.client.get(
            reverse("apply:apply", kwargs={"pk": self.job.id})
        )
        self.assertEqual(response.status_code, 200)

    def test_form_passed_in_context_candidate(self):
        self.login_candidate()
        response = self.client.get(
            reverse("apply:apply", kwargs={"pk": self.job.id})
        )
        self.assertTrue("form" in response.context)
        self.assertIsInstance(response.context["form"], ApplicationForm)

    def test_bad_POST_redirects_to_same_page(self):
        self.login_candidate()
        response = self.client.post(
            reverse("apply:apply", kwargs={"pk": self.job.id}),
            data={
                "first_name": test_user_data["candidate"]["profile"]["first_name"],
                "last_name": test_user_data["candidate"]["profile"]["last_name"],
                "address_line": test_user_data["candidate"]["profile"]["address_line"],
                "zip_code": test_user_data["candidate"]["profile"]["zip_code"],
                "state": test_user_data["candidate"]["profile"]["state"],
                "email": test_user_data["candidate"]["profile"]["email"],
                "phone": test_user_data["candidate"]["profile"]["phone"],
                "portfolio_website": test_user_data["candidate"]["profile"][
                    "portfolio_website"],
                "education": test_user_data["candidate"]["profile"]["education"],
                "experiences": test_user_data["candidate"]["profile"]["experiences"],
                "cover_letter": test_user_data["candidate"]["profile"]["cover_letter"],
                "gender": test_user_data["candidate"]["profile"]["gender"],
                "ethnicity": test_user_data["candidate"]["profile"]["ethnicity"],
                "race": test_user_data["candidate"]["profile"]["race"],
                "health_conditions": test_user_data["candidate"]["profile"][
                    "health_conditions"],
                "veteran": test_user_data["candidate"]["profile"]["veteran"],
                "update_profile": False,
            }, follow=True,
        )
        self.assertRedirects(response, reverse("apply:apply", kwargs={"pk": self.job.id}), status_code=302)
        self.assertEqual(Application.objects.all().count(), 0)

    """
    # Fails with 302 error
    def test_good_post(self):
        self.login_candidate()
        response = self.client.post(
            reverse("apply:apply", kwargs={"pk": self.job.id}), data=test_user_data["candidate"]["profile"],
        )
        self.assertEquals(response.status_code, 200)
    """