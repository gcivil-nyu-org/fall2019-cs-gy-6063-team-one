import datetime
from decimal import Decimal

from django.db.models.query import QuerySet
from django.test import TestCase
from django.urls import reverse

from jobs.models import Job, Department, SavedJobs
from jobs.views import JobsView

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
class JobsViewSideCandidateTest(TestCase):
    q = ""

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
        self.login_candidate()

    def create_department(self):
        return Department.objects.create(name="department")

    def create_job(self):
        department = self.create_department()
        job = Job(
            id="87990",
            department=department,
            business_title="Account Manager",
            civil_service_title="'CONTRACT REVIEWER (OFFICE OF L",
            title_code_no="40563",
            level="1",
            job_category="",
            ft_pt_indicator="",
            salary_start=Decimal("42405.0000000000"),
            salary_end=Decimal("65485.0000000000"),
            salary_frequency="Annual",
            work_location="110 William St. N Y",
            division="Strategy & Analytics",
            job_description="Spend time working on accounts. Use a calculator.",
            min_qualifications="1.\tA baccalaureate degree \
            from an accredited college and\
             two years of experience in community \
             work or community centered activities in\
              an area related to the duties described \
              above; or  2.\tHigh school graduation\
               or equivalent",
            preferred_skills="Excellent interpersonal and \
            organizational skills",
            additional_info="",
            to_apply="For DoITT Employees Only  Please go to \
            Employee Self Service (ESS), \
            click on Recruiting Activities > Careers, and \
            search for Job ID #184328  -or-   \
            If you do not have access to a computer, \
            please mail resume indicating Job ID # to:  \
            Department of Information Technology and \
            Telecommunications (DoITT)  Recruitment Office\
             - 255 Greenwich Street - 9th Floor - New York,\
              NY 10007    SUBMISSION OF A RESUME \
             IS NOT A GUARANTEE THAT YOU WILL RECEIVE \
             AN INTERVIEW  APPOINTMENTS ARE SUBJECT TO \
             OVERSIGHT APPROVAL",
            hours_info="Day - Due to the necessary \
            technical management duties of this position \
            in a 24/7 operation, candidate may be \
            required to be on call and/or work various \
            shifts such as weekends and/or nights/evenings.",
            secondary_work_location="Brooklyn, NY",
            recruitment_contact="",
            residency_requirement="New York City Residency \
            is not required for this position",
            posting_date=datetime.date(2015, 2, 19),
            post_until=None,
            posting_updated=datetime.date(2015, 2, 19),
            process_date=datetime.date(2019, 10, 15),
        )
        job.save()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/jobs/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_is_accessible_by_name(self):
        response = self.client.get(reverse("jobs:jobs"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("jobs:jobs"))
        self.assertTemplateUsed(response, "uplyft/base.html")
        self.assertTemplateUsed(response, "jobs/jobs.html")

    def test_form_GET_response_renders_correct_template(self):
        response = self.client.get(reverse("jobs:jobs"), data={})
        self.assertTemplateUsed(response, "uplyft/base.html")
        self.assertTemplateUsed(response, "jobs/jobs.html")

    def test_form_GET_response_returns_queryset_in_context(self):
        response = self.client.get(reverse("jobs:jobs"), data={})
        self.assertIsInstance(response.context["jobs"], QuerySet)

    def test_form_GET_response_returns_correct_view_in_context(self):
        response = self.client.get(reverse("jobs:jobs"), data={})
        self.assertIsInstance(response.context["view"], JobsView)

    def test_form_GET_response_returns_a_queryset(self):
        response = self.client.get(reverse("jobs:jobs"), data={})
        self.assertTrue("jobs" in response.context)
        self.assertIsInstance(response.context["jobs"], QuerySet)

    def test_form_GET_response_retains_form_data(self):
        response = self.client.get(
            reverse("jobs:jobs"), data={"business_title": "manager"}
        )
        self.assertContains(response, "manager")

    def test_good_GET_response_returns_correct_queryset(self):
        self.create_job()
        response = self.client.get(reverse("jobs:jobs"), data={})
        correct_queryset = Job.objects.all().order_by("-posting_date")
        self.assertListEqual(list(correct_queryset), list(response.context["jobs"]))

    def test_good_GET_response_returns_correct_queryset_with_business_title(self):
        self.create_job()
        response = self.client.get(
            reverse("jobs:jobs"), data={"business_title": "manager"}
        )
        correct_queryset = Job.objects.filter(
            business_title__icontains="manager"
        ).order_by("-posting_date")
        self.assertListEqual(list(correct_queryset), list(response.context["jobs"]))

    def test_good_GET_response_returns_correct_queryset_with_description(self):
        self.create_job()
        response = self.client.get(
            reverse("jobs:jobs"), data={"description": "calculator"}
        )
        correct_queryset = Job.objects.filter(
            job_description__icontains="calculator"
        ).order_by("-posting_date")
        self.assertListEqual(list(correct_queryset), list(response.context["jobs"]))

    def test_candidate_save_unsave_job(self):
        _ = self.client.get(reverse("jobs:save_job", kwargs={"pk": self.job.id}))
        record = SavedJobs.objects.filter(user=self.candidate.user, job=self.job)
        self.assertEqual(record.count(), 1)

        _ = self.client.get(reverse("jobs:save_job", kwargs={"pk": self.job.id}))
        record = SavedJobs.objects.filter(user=self.candidate.user, job=self.job)
        self.assertEqual(record.count(), 0)

        _ = self.client.get(reverse("jobs:save_job", kwargs={"pk": self.job.id}))
        record = SavedJobs.objects.filter(user=self.candidate.user, job=self.job)
        self.assertEqual(record.count(), 1)

        _ = self.client.get(reverse("jobs:save_job", kwargs={"pk": self.job.id}))
        record = SavedJobs.objects.filter(user=self.candidate.user, job=self.job)
        self.assertEqual(record.count(), 0)

    def test_view_return_load_jobs_page(self):
        self.login_candidate()
        response = self.client.get(reverse("jobs:load_jobs"))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse("jobs:load_jobs"))
        self.assertEqual(response.status_code, 200)
