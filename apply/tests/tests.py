from django.test import TestCase
from django.urls import reverse
from decimal import Decimal
from django.utils.html import escape
import datetime
from apply.forms import JobApplicationForm
from apply.models import Application
from jobs.models import Job
from tests.tests import valid_data, invalid_data
from uplyft.models import CustomUser
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login


class ApplyViewTests(TestCase):
    def login(self):
        return authenticate(email=valid_data["email"], password=valid_data["password"])

    def setUp(self):
        get_user_model().objects.create(
            first_name=valid_data["first_name"],
            last_name=valid_data["last_name"],
            email=valid_data["email"],
            password=valid_data["password"],
        )
        Job.objects.create(
            job_id=1,
            agency="DEPARTMENT OF BUSINESS SERV.",
            posting_type="Internal",
            business_title="Account Manager",
            civil_service_title="CONTRACT REVIEWER (OFFICE OF L",
            title_code_no="40563",
            level="1",
            job_category="",
            ft_pt_indicator="",
            salary_start=Decimal('42405.0000000000'),
            salary_end=Decimal('65485.0000000000'),
            salary_frequency="Annual",
            work_location="110 William St. N Y",
            division="Strategy & Analytics",
            job_description="The Account Manager will oversee a \
                         portfolio of several City agencies and will be \
                         responsible for the monitoring and oversight of \
                         the strategies which have been broadly laid out \
                         for agencies to increase M/WBE utilization.  The \
                         primary objective for the Account Manager is to help \
                         agencies increase the number and dollar value of \
                         contracts awarded to M/WBE at various contract levels.",
            min_qualifications="1.\tA baccalaureate degree from an accredited college ",
            preferred_skills="Excellent interpersonal and organizational skills.",
            additional_info="Salary range for this position is: $42,405 - $45,000 per year",
            to_apply="",
            hours_info="",
            secondary_work_location="",
            recruitment_contact="",
            residency_requirement="New York City residency is generally required within 90 days of appointment.",
            posting_date=datetime.date(2011, 6, 24),
            post_until=None,
            posting_updated=datetime.date(2011, 6, 24),
            process_date=datetime.date(2019, 10, 15),
        )

    def test_view_is_not_directly_accessible_by_GET(self):
        response = self.client.get(reverse("apply:apply"))
        self.assertNotEqual(response.status_code, 200)

    def test_view_is_not_directly_accessible_by_POST(self):
        response = self.client.post(reverse("apply:apply"), data={"job_id": 1})
        self.assertNotEqual(response.status_code, 200)

    def test_login_required_fail(self):
        response = self.client.get("/jobs/1")
        self.assertNotEquals(response.status_code, 200)

    def test_login_required_pass(self):
        user = self.login()
        response = self.client.get("/jobs/1")
        self.assertEquals(response.status_code, 200)




