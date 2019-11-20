from django.test import TestCase
from django.urls import reverse
from uplyft.tests.resources import (
    test_user_data,
    create_job,
    create_application,
    create_candidate_with_active_profile,
    create_department,
    create_department_with_profile,
    create_employer,
)
from jobs.models import Job
from apply.models import Application


class DepartmentDetailViewTest(TestCase):
    def setUp(self):
        self.department = create_department_with_profile(test_user_data["department"])
        self.employer = create_employer(self.department, test_user_data["employer"])
        self.candidate = create_candidate_with_active_profile(
            test_user_data["candidate"]
        )

        self.other_candidates = []
        for test_candidate in test_user_data["candidates"]:
            self.other_candidates.append(
                create_candidate_with_active_profile(test_candidate)
            )

        self.job1 = create_job(self.department, test_user_data["job_details"][0])
        self.apps = []
        for other_candidate in self.other_candidates:
            self.apps.append(
                create_application(
                    self.job1, other_candidate, other_candidate.candidate_profile
                )
            )

        self.job2 = create_job(self.department, test_user_data["job_details"][1])
        self.apps.append(
            create_application(
                self.job2,
                self.other_candidates[0],
                self.other_candidates[0].candidate_profile,
            )
        )

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
        response = self.client.get(
            reverse(
                "department_details:department_detail",
                kwargs={"pk": self.department.id},
            )
        )
        self.assertEqual(response.status_code, 302)

    def test_view_accessible_to_candidate_by_name_and_pk(self):
        self.login_candidate()
        response = self.client.get(
            reverse(
                "department_details:department_detail",
                kwargs={"pk": self.department.id},
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_view_accessible_to_employer_by_name_and_pk(self):
        self.login_employer()
        response = self.client.get(
            reverse(
                "department_details:department_detail",
                kwargs={"pk": self.department.id},
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template_candidate(self):
        self.login_candidate()
        response = self.client.get(
            reverse(
                "department_details:department_detail",
                kwargs={"pk": self.department.id},
            )
        )
        self.assertTemplateUsed(response, "uplyft/base.html")
        self.assertTemplateUsed(response, "department_details/department_detail.html")

    def test_view_uses_correct_template_employer(self):
        self.login_employer()
        response = self.client.get(
            reverse(
                "department_details:department_detail",
                kwargs={"pk": self.department.id},
            )
        )
        self.assertTemplateUsed(response, "uplyft/base.html")
        self.assertTemplateUsed(response, "department_details/department_detail.html")

    def test_view_returns_jobs_associated_with_current_department_candidate(self):
        self.login_candidate()
        response = self.client.get(
            reverse(
                "department_details:department_detail",
                kwargs={"pk": self.department.id},
            )
        )
        self.assertEqual(response.status_code, 200)
        jobs_in_this_department = Job.objects.filter(department=self.department)
        for job in jobs_in_this_department:
            self.assertContains(response, job.id)
            self.assertContains(response, job.business_title)
            self.assertContains(response, job.posting_date.strftime("%m/%d/%y"))

    def test_view_returns_jobs_associated_with_current_department_employer(self):
        self.login_employer()
        response = self.client.get(
            reverse(
                "department_details:department_detail",
                kwargs={"pk": self.department.id},
            )
        )
        self.assertEqual(response.status_code, 200)
        jobs_in_this_department = Job.objects.filter(department=self.department)
        for job in jobs_in_this_department:
            self.assertContains(response, job.id)
            self.assertContains(response, job.business_title)
            self.assertContains(response, job.posting_date.strftime("%m/%d/%y"))

    def test_context_has_count_of_submitted_applications_candidate(self):
        self.login_candidate()
        response = self.client.get(
            reverse(
                "department_details:department_detail",
                kwargs={"pk": self.department.id},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue("submitted_applications_data" in response.context)

        apps_to_job1 = Application.objects.filter(job=self.job1).count()
        apps_to_job2 = Application.objects.filter(job=self.job2).count()

        self.assertEquals(
            response.context["submitted_applications_data"][self.job1.id], apps_to_job1
        )
        self.assertEquals(
            response.context["submitted_applications_data"][self.job2.id], apps_to_job2
        )

    def test_context_has_count_of_submitted_applications_employer(self):
        self.login_employer()
        response = self.client.get(
            reverse(
                "department_details:department_detail",
                kwargs={"pk": self.department.id},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue("submitted_applications_data" in response.context)

        apps_to_job1 = Application.objects.filter(job=self.job1).count()
        apps_to_job2 = Application.objects.filter(job=self.job2).count()

        self.assertEquals(
            response.context["submitted_applications_data"][self.job1.id], apps_to_job1
        )
        self.assertEquals(
            response.context["submitted_applications_data"][self.job2.id], apps_to_job2
        )

    def test_context_displays_department_profile_details_labels_if_exists(self):
        self.login_employer()
        response = self.client.get(
            reverse(
                "department_details:department_detail",
                kwargs={"pk": self.department.id},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Description")
        self.assertContains(response, "Website")
        self.assertContains(response, "Address")

    def test_context_hides_department_profile_details_labels_if_not_exists(self):
        self.login_employer()
        self.department_with_no_profile = create_department(
            test_user_data["department_with_no_profile"])
        response = self.client.get(
            reverse(
                "department_details:department_detail",
                kwargs={"pk": self.department_with_no_profile.id},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Description")
        self.assertNotContains(response, "Website")
        self.assertNotContains(response, "Address")
