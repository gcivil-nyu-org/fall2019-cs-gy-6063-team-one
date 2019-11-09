import datetime
from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from apply.models import Application
from jobs.models import Department, Job
from uplyft.models import CustomUser, Employer, Candidate, CandidateProfile

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

valid_users = [
    {
        "employer1",
        {
            "first_name": "Alex",
            "last_name": "Rodriguez",
            "email": "username@gmail.com",
            "password": "'LKlk#fvdf94@78!9"
        }
    },
    {
        "candidate1",
        {
            "first_name": "Jane",
            "last_name": "Jameson",
            "email": "jane@example.com",
            "password": "cN3KJXi4GxsCxZET"
        }
    }
]

user_data_invalid = {
    "first_name": "*((*&",
    "last_name": "123",
    "email": "response@edu",
    "password": "103348494",
}

candidate_valid = {
    "first_name": user_data_valid["first_name"],
    "last_name": user_data_valid["last_name"],
    "email": user_data_valid["email"],
    "password1": user_data_valid["password1"],
    "password2": user_data_valid["password2"],
}

candidate_invalid_first_name = {
    "first_name": user_data_invalid["first_name"],
    "last_name": user_data_valid["last_name"],
    "email": user_data_valid["email"],
    "password1": user_data_valid["password"],
    "password2": user_data_valid["password"],
}

candidate_invalid_last_name = {
    "first_name": user_data_valid["first_name"],
    "last_name": user_data_invalid["last_name"],
    "email": user_data_valid["email"],
    "password1": user_data_valid["password"],
    "password2": user_data_valid["password"],
}

candidate_invalid_email = {
    "first_name": user_data_valid["first_name"],
    "last_name": user_data_valid["last_name"],
    "email": user_data_invalid["email"],
    "password1": user_data_valid["password"],
    "password2": user_data_valid["password"],
}

candidate_invalid_password1 = {
    "first_name": user_data_valid["first_name"],
    "last_name": user_data_valid["last_name"],
    "email": user_data_valid["email"],
    "password1": user_data_invalid["password"],
    "password2": user_data_valid["password"],
}

candidate_invalid_password2 = {
    "first_name": user_data_valid["first_name"],
    "last_name": user_data_valid["last_name"],
    "email": user_data_valid["email"],
    "password1": user_data_valid["password"],
    "password2": user_data_invalid["password"],
}

candidate_invalid_password_mismatch = {
    "first_name": user_data_valid["first_name"],
    "last_name": user_data_valid["last_name"],
    "email": user_data_valid["email"],
    "password1": user_data_valid["password"],
    "password2": user_data_valid["password"] + "!",
}


def POST_to_view(self, view, data):
    return self.client.post(reverse(view), data=data)

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
    profile = CandidateProfile.objects.create()
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