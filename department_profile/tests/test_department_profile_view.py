from django.test import TestCase
from django.urls import reverse
from uplyft.tests.resources import (
    test_user_data,
    create_department,
    create_department_with_profile,
    create_employer,
)
from jobs.models import DepartmentProfile


class DepartmentProfileViewTest(TestCase):
    def login_employer(self):
        self.client.login(
            email=test_user_data["employer"]["email"],
            password=test_user_data["employer"]["password"],
        )

    def login_employer_with_department_profile(self):
        self.client.login(
            email=test_user_data["candidate"]["email"],
            password=test_user_data["candidate"]["password"],
        )

    def setUp(self):
        self.department = create_department(
            test_user_data["department_with_no_profile"]
        )
        self.employer = create_employer(self.department, test_user_data["employer"])

    def test_view_exists_at_desired_location(self):
        self.login_employer()
        response = self.client.get("/department_profile/")
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_by_name(self):
        self.login_employer()
        response = self.client.get(
            reverse("department_profile:update_department_profile")
        )
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        self.login_employer()
        response = self.client.get(
            reverse("department_profile:update_department_profile")
        )
        self.assertTemplateUsed(response, "uplyft/base.html")
        self.assertTemplateUsed(response, "department_profile/department_profile.html")

    def test_view_contains_form_labels(self):
        self.login_employer()
        response = self.client.get(
            reverse("department_profile:update_department_profile")
        )
        self.assertContains(response, "Description")
        self.assertContains(response, "Website")
        self.assertContains(response, "Address")

    def test_view_contains_profile_data_if_exists(self):
        self.department_with_profile = create_department_with_profile(
            test_user_data["department"]
        )
        self.employer_with_department_profile = create_employer(
            self.department_with_profile, test_user_data["candidate"]
        )
        self.login_employer_with_department_profile()
        response = self.client.get(
            reverse("department_profile:update_department_profile")
        )
        self.assertContains(response, "Description")
        self.assertContains(response, "Website")
        self.assertContains(response, "Address")
        self.assertContains(
            response, self.department_with_profile.department_profile.description
        )
        self.assertContains(
            response, self.department_with_profile.department_profile.website
        )
        self.assertContains(
            response, self.department_with_profile.department_profile.address
        )

    def test_view_good_POST_displays_data_and_redirects_to_details_view_with_data(self):
        self.login_employer()
        response = self.client.post(
            reverse("department_profile:update_department_profile"),
            data={
                "description": test_user_data["department"]["profile"]["description"],
                "website": test_user_data["department"]["profile"]["website"],
                "address": test_user_data["department"]["profile"]["address"],
            },
        )
        self.assertRedirects(
            response,
            reverse(
                "department_details:department_detail",
                kwargs={"pk": self.department.id},
            ),
            status_code=302,
        )
        self.assertEqual(DepartmentProfile.objects.all().count(), 1)
        updated_profile_details = self.client.get(
            reverse(
                "department_details:department_detail",
                kwargs={"pk": self.department.id},
            )
        )
        self.assertEqual(updated_profile_details.status_code, 200)
        self.assertContains(
            updated_profile_details,
            test_user_data["department"]["profile"]["description"],
        )
        self.assertContains(
            updated_profile_details, test_user_data["department"]["profile"]["website"]
        )
        self.assertContains(
            updated_profile_details, test_user_data["department"]["profile"]["address"]
        )
