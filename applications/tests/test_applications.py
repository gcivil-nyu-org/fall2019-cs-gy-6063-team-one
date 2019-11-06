from django.test import TestCase
from django.urls import reverse
from uplyft.models import CustomUser
from jobs.models import Job, Department
from apply.models import Application
from uplyft.models import Candidate, Employer, CandidateProfile
from applications.forms import ProcessApplicationForm
import datetime
from decimal import Decimal

foo_employer = {
    "first_name": "John",
    "last_name": "Johnson",
    "email": "john@example.com",
    "password": "cN3KJXi4GxsCxZET",
}

foo_candidate = {
    "first_name": "Jane",
    "last_name": "Jameson",
    "email": "jane@example.com",
    "password": "cN3KJXi4GxsCxZET",
}

foo_candidate_profile = {
    "first_name": "Jane",
    "last_name": "Jameson",
    "email": "jane@example.com",
    "gender": "X",
    "ethnicity": "OT",
    "race": "ASIAN",
    "health_conditions": "POSITIVE",
    "veteran": "POSITIVE",
    "address_line": "123 Main Street, Hoboken",
    "zip_code": "07030",
    "state": "NJ",
    "phone": "2018347135",
    "portfolio_website": "https://janejameson.com",
    "cover_letter": "Please hire me, I need this job",
    "experiences": "Nada",
    "education": "Self-taught",
    "additional_info": "Good listener",
}


def create_department():
    return Department.objects.create(id=1, name="NYC Fire")


def create_employer(department):
    cu = CustomUser.objects.create_user(
        email=foo_employer["email"],
        password=foo_employer["password"],
        first_name=foo_employer["first_name"],
        last_name=foo_employer["last_name"],
    )
    return Employer.objects.create(user=cu, department=department)


def create_candidate():
    cu = CustomUser.objects.create_user(
        email=foo_candidate["email"],
        password=foo_candidate["password"],
        first_name=foo_candidate["first_name"],
        last_name=foo_candidate["last_name"],
        is_candidate=True,
    )
    profile = CandidateProfile.objects.create(
        email=foo_candidate["email"],
        first_name=foo_candidate["first_name"],
        last_name=foo_candidate["last_name"],
    )
    return Candidate.objects.create(user=cu, candidate_profile=profile)


def create_job(department):
    return Job.objects.create(
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
        min_qualifications="Quals",
        preferred_skills="skills",
        additional_info="",
        to_apply="apply",
        hours_info="some hours",
        secondary_work_location="Brooklyn, NY",
        recruitment_contact="",
        residency_requirement="some reqs",
        posting_date=datetime.date(2015, 2, 19),
        post_until=None,
        posting_updated=datetime.date(2015, 2, 19),
        process_date=datetime.date(2019, 10, 15),
    )


def create_application(job, candidate):
    return Application.objects.create(job=job, candidate=candidate)


class ApplicationDetailsViewTests(TestCase):
    def login_candidate(self):
        self.client.login(
            email=foo_candidate["email"], password=foo_candidate["password"]
        )

    def login_employer(self):
        self.client.login(
            email=foo_employer["email"], password=foo_employer["password"]
        )

    def setUp(self):
        self.department = create_department()
        self.employer = create_employer(self.department)
        self.candidate = create_candidate()
        self.job = create_job(self.department)
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

    def test_GET_displays_application_details_candidate(self):
        self.login_candidate()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(response, self.candidate.candidate_profile.first_name)
        self.assertContains(response, self.candidate.candidate_profile.last_name)
        self.assertContains(response, self.candidate.candidate_profile.gender)
        self.assertContains(response, self.candidate.candidate_profile.ethnicity)
        self.assertContains(response, self.candidate.candidate_profile.race)
        self.assertContains(
            response, self.candidate.candidate_profile.health_conditions
        )
        self.assertContains(response, self.candidate.candidate_profile.veteran)
        self.assertContains(response, self.candidate.candidate_profile.address_line)
        self.assertContains(response, self.candidate.candidate_profile.zip_code)
        self.assertContains(response, self.candidate.candidate_profile.state)
        self.assertContains(response, self.candidate.candidate_profile.phone)
        self.assertContains(response, self.candidate.candidate_profile.email)
        self.assertContains(
            response, self.candidate.candidate_profile.portfolio_website
        )
        self.assertContains(response, self.candidate.candidate_profile.cover_letter)
        self.assertContains(response, self.candidate.candidate_profile.experiences)
        self.assertContains(response, self.candidate.candidate_profile.additional_info)

    def test_GET_displays_application_details_employer(self):
        self.login_employer()
        response = self.client.get(
            reverse("applications:application_details", kwargs={"pk": self.app.id})
        )
        self.assertContains(response, self.candidate.candidate_profile.first_name)
        self.assertContains(response, self.candidate.candidate_profile.last_name)
        self.assertContains(response, self.candidate.candidate_profile.gender)
        self.assertContains(response, self.candidate.candidate_profile.ethnicity)
        self.assertContains(response, self.candidate.candidate_profile.race)
        self.assertContains(
            response, self.candidate.candidate_profile.health_conditions
        )
        self.assertContains(response, self.candidate.candidate_profile.veteran)
        self.assertContains(response, self.candidate.candidate_profile.address_line)
        self.assertContains(response, self.candidate.candidate_profile.zip_code)
        self.assertContains(response, self.candidate.candidate_profile.state)
        self.assertContains(response, self.candidate.candidate_profile.phone)
        self.assertContains(response, self.candidate.candidate_profile.email)
        self.assertContains(
            response, self.candidate.candidate_profile.portfolio_website
        )
        self.assertContains(response, self.candidate.candidate_profile.cover_letter)
        self.assertContains(response, self.candidate.candidate_profile.experiences)
        self.assertContains(response, self.candidate.candidate_profile.additional_info)
