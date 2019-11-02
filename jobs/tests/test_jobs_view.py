import datetime
from decimal import Decimal

from django.db.models.query import QuerySet
from django.test import TestCase
from django.urls import reverse

from jobs.models import Job, Department
from jobs.views import JobsView


class JobsViewTest(TestCase):
    q = ""

    def create_department(self):
        return Department.objects.create(name="department")

    def create_job(self):
        department = self.create_department()
        job = Job(
            job_id="87990",
            department=department,
            posting_type="Internal",
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
            job_description="Some text.",
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
        response = self.client.get(reverse("jobs:jobs"), data={"q": self.q})
        self.assertTemplateUsed(response, "uplyft/base.html")
        self.assertTemplateUsed(response, "jobs/jobs.html")

    def test_form_GET_response_returns_queryset_in_context(self):
        response = self.client.get(reverse("jobs:jobs"), data={"q": self.q})
        self.assertIsInstance(response.context["jobs"], QuerySet)

    def test_form_GET_response_returns_correct_view_in_context(self):
        response = self.client.get(reverse("jobs:jobs"), data={"q": self.q})
        self.assertIsInstance(response.context["view"], JobsView)

    def test_form_GET_response_returns_a_queryset(self):
        response = self.client.get(reverse("jobs:jobs"), data={"q": self.q})
        self.assertTrue("jobs" in response.context)
        self.assertIsInstance(response.context["jobs"], QuerySet)

    def test_form_GET_response_retains_form_data(self):
        response = self.client.get(reverse("jobs:jobs"), data={"q": "manager"})
        self.assertContains(response, "manager")

    def test_good_GET_response_returns_correct_queryset(self):
        self.create_job()
        response = self.client.get(reverse("jobs:jobs"), data={"q": self.q})
        correct_queryset = Job.objects.all().order_by("-posting_date")
        self.assertListEqual(list(correct_queryset), list(response.context["jobs"]))
