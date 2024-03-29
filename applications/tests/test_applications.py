from django.test import TestCase
from django.urls import reverse
from applications.forms import ProcessApplicationForm
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
from apply.models import Application


@setUpMockedS3
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
        self.candidate = create_candidate_with_active_profile(
            test_user_data["candidate"]
        )
        self.department = create_department(test_user_data["department"])
        self.employer = create_employer(self.department, test_user_data["employer"])
        self.job = create_job(self.department, test_user_data["job_details"][0])
        self.profile = create_profile(test_user_data["candidate"]["profile"])
        self.app = create_application(self.job, self.candidate, self.profile)

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

    def test_GET_displays_first_name_to_candidate(self):
        self.login_candidate()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(response, self.app.candidate_profile.first_name)

    def test_GET_displays_last_name_to_candidate(self):
        self.login_candidate()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(response, self.app.candidate_profile.last_name)

    def test_GET_displays_gender_to_candidate(self):
        self.login_candidate()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(response, self.app.candidate_profile.get_gender_display())

    def test_GET_displays_ethnicity_to_candidate(self):
        self.login_candidate()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(
            response, self.app.candidate_profile.get_ethnicity_display()
        )

    def test_GET_displays_race_to_candidate(self):
        self.login_candidate()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(response, self.app.candidate_profile.get_race_display())

    def test_GET_displays_health_conditions_to_candidate(self):
        self.login_candidate()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(
            response, self.app.candidate_profile.get_health_conditions_display()
        )

    def test_GET_displays_veteran_to_candidate(self):
        self.login_candidate()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(response, self.app.candidate_profile.get_veteran_display())

    def test_GET_displays_address_to_candidate(self):
        self.login_candidate()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(response, self.app.candidate_profile.address_line)

    def test_GET_displays_state_to_candidate(self):
        self.login_candidate()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(response, self.app.candidate_profile.state)

    def test_GET_displays_phone_to_candidate(self):
        self.login_candidate()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        # Had to hard code until I figure out how to retrieve the data in this format
        self.assertContains(response, self.app.candidate_profile.phone)

    def test_GET_displays_email_to_candidate(self):
        self.login_candidate()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(response, self.app.candidate_profile.email)

    def test_GET_displays_portfolio_website_to_candidate(self):
        self.login_candidate()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(response, self.app.candidate_profile.portfolio_website)

    def test_GET_displays_cover_letter_to_candidate(self):
        self.login_candidate()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(response, self.app.candidate_profile.cover_letter)

    def test_GET_displays_resume_to_candidate(self):
        self.login_candidate()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(response, self.app.candidate_profile.resume)

    def test_GET_displays_first_name_to_employer(self):
        self.login_employer()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(response, self.app.candidate_profile.first_name)

    def test_GET_displays_last_name_to_employer(self):
        self.login_employer()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(response, self.app.candidate_profile.last_name)

    def test_GET_displays_gender_to_employer(self):
        self.login_employer()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(response, self.app.candidate_profile.get_gender_display())

    def test_GET_displays_ethnicity_to_employer(self):
        self.login_employer()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(
            response, self.app.candidate_profile.get_ethnicity_display()
        )

    def test_GET_displays_race_to_employer(self):
        self.login_employer()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(response, self.app.candidate_profile.get_race_display())

    def test_GET_displays_health_conditions_to_employer(self):
        self.login_employer()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(
            response, self.app.candidate_profile.get_health_conditions_display()
        )

    def test_GET_displays_veteran_to_employer(self):
        self.login_employer()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(response, self.app.candidate_profile.get_veteran_display())

    def test_GET_displays_address_to_employer(self):
        self.login_employer()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(response, self.app.candidate_profile.address_line)

    def test_GET_displays_state_to_employer(self):
        self.login_employer()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(response, self.app.candidate_profile.state)

    def test_GET_displays_phone_to_employer(self):
        self.login_employer()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        # Had to hard code until I figure out how to retrieve the data in this format
        self.assertContains(response, self.app.candidate_profile.phone)

    def test_GET_displays_email_to_employer(self):
        self.login_employer()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(response, self.app.candidate_profile.email)

    def test_GET_displays_portfolio_website_to_employer(self):
        self.login_employer()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(response, self.app.candidate_profile.portfolio_website)

    def test_GET_displays_cover_letter_to_employer(self):
        self.login_employer()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(response, self.app.candidate_profile.cover_letter)

    def test_GET_displays_resume_to_employer(self):
        self.login_employer()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(response, self.app.candidate_profile.resume)

    def test_other_candidate_cannot_view_application(self):
        # create other candidate
        self.other_candidate = create_candidate_with_active_profile(
            test_user_data["candidates"][1]
        )
        # login other candidate
        self.client.login(
            email=test_user_data["candidates"][1]["email"],
            password=test_user_data["candidates"][1]["password"],
        )
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(
            response, "You do not have the right permissions to view this page"
        )

    def test_non_department_employer_cannot_view_application(self):
        other_department = create_department(test_user_data["departments"][1])
        create_employer(other_department, test_user_data["employers"][1])
        self.client.login(
            email=test_user_data["employers"][1]["email"],
            password=test_user_data["employers"][1]["password"],
        )
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(
            response, "You do not have the right permissions to view this page"
        )

    def test_employer_can_accept_application(self):
        self.login_employer()
        self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertTrue(self.app.status == Application.STATUS_APPLIED)
        self.client.post(
            reverse("applications:application_details", kwargs={"pk": self.app.id}),
            data={"accept_button": "Accept"},
        )
        self.app = Application.objects.get(pk=self.app.id)
        self.assertTrue(self.app.status == Application.STATUS_ACCEPTED)

    def test_employer_can_reject_application(self):
        self.login_employer()
        self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertTrue(self.app.status == Application.STATUS_APPLIED)
        self.client.post(
            reverse("applications:application_details", kwargs={"pk": self.app.id}),
            data={"reject_button": "Reject"},
        )
        self.app = Application.objects.get(pk=self.app.id)
        self.assertTrue(self.app.status == Application.STATUS_REJECTED)

    def test_anonymous_user_cannot_process_application(self):
        response = self.client.post(
            reverse("applications:application_details", kwargs={"pk": self.app.id}),
            data={"accept_button": "Accept"},
        )
        expected_url = (
            reverse("candidate_login:candidate_login")
            + "?next="
            + reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertRedirects(
            response, expected_url, status_code=302, target_status_code=200
        )
