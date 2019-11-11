from django.test import TestCase
from django.urls import reverse
from applications.forms import ProcessApplicationForm
from uplyft.tests.resources import (
    create_department,
    create_job,
    create_application,
    create_candidate,
    create_employer,
    test_user_data,
)


class ApplicationDetailsViewTests(TestCase):
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
        self.department = create_department(test_user_data["department"])
        self.employer = create_employer(self.department, test_user_data["employer"])
        self.candidate = create_candidate(test_user_data["candidate"])
        self.job = create_job(self.department, test_user_data["job_details"][0])
        self.app = create_application(self.job, self.candidate)

    def test_view_url_is_accessible_by_name_candidate(self):
        self.login_candidate()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertEqual(response.status_code, 200)

    def test_view_url_is_accessible_by_name_employer(self):
        self.login_employer()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template_candidate(self):
        self.login_candidate()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "uplyft/base.html")
        self.assertTemplateUsed(response, "applications/application_detail.html")

    def test_view_uses_correct_template_employer(self):
        self.login_employer()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "uplyft/base.html")
        self.assertTemplateUsed(response, "applications/application_detail.html")

    def test_form_passed_in_context_employer(self):
        self.login_employer()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertTrue("form" in response.context)
        self.assertIsInstance(response.context["form"], ProcessApplicationForm)

    def test_form_NOT_passed_in_context_candidate(self):
        self.login_candidate()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertTrue("form" in response.context)
        self.assertEquals(response.context["form"], None)

    # def test_GET_displays_application_details_candidate(self):
    #     self.login_candidate()
    #     response = self.client.get(
    #         reverse("applications:application_details", kwargs={"pk": self.app.id})
    #     )
    #
    #     expected = [
    #         self.app.candidate_profile.first_name,
    #         self.app.candidate_profile.last_name,
    #         self.app.candidate_profile.get_gender_display(),
    #         self.app.candidate_profile.get_ethnicity_display(),
    #         self.app.candidate_profile.get_race_display(),
    #         self.app.candidate_profile.get_health_conditions_display(),
    #         self.app.candidate_profile.get_veteran_display(),
    #         self.app.candidate_profile.address_line,
    #         self.app.candidate_profile.zip_code,
    #         self.app.candidate_profile.state,
    #         self.app.candidate_profile.phone,
    #         self.app.candidate_profile.email,
    #         self.app.candidate_profile.portfolio_website,
    #         self.app.candidate_profile.cover_letter,
    #         self.app.candidate_profile.experiences,
    #         #self.app.candidate_profile.additional_info,
    #     ]
    #
    #     for item in expected:
    #         self.assertContains(response, item)
    #
    # def test_GET_displays_application_details_employer(self):
    #     self.login_employer()
    #     response = self.client.get(
    #         reverse("applications:application_details", kwargs={"pk": self.app.id})
    #     )
    #
    #     expected = [
    #         self.app.candidate_profile.first_name,
    #         self.app.candidate_profile.last_name,
    #         self.app.candidate_profile.get_gender_display(),
    #         self.app.candidate_profile.get_ethnicity_display(),
    #         self.app.candidate_profile.get_race_display(),
    #         self.app.candidate_profile.get_health_conditions_display(),
    #         self.app.candidate_profile.get_veteran_display(),
    #         self.app.candidate_profile.address_line,
    #         self.app.candidate_profile.zip_code,
    #         self.app.candidate_profile.state,
    #         self.app.candidate_profile.phone,
    #         self.app.candidate_profile.email,
    #         self.app.candidate_profile.portfolio_website,
    #         self.app.candidate_profile.cover_letter,
    #         self.app.candidate_profile.experiences,
    #         #self.app.candidate_profile.additional_info,
    #     ]
    #
    #     for item in expected:
    #         self.assertContains(response, item)
