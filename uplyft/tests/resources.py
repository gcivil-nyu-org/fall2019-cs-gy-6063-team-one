import datetime
from decimal import Decimal

from django.test import TestCase
from django.urls import reverse

from apply.models import Application
from jobs.models import Department, Job
from uplyft.models import CustomUser, Employer, Candidate, CandidateProfile

user_data = {
    "valid": {
        "user1": {
            "first_name": "Jane",
            "last_name": "Jameson",
            "email": "jane@example.com",
            "password": "cN3KJXi4GxsCxZET"
        },
        "user2": {
            "first_name": "Alex",
            "last_name": "Rodriguez",
            "email": "username@gmail.com",
            "password": "'LKlk#fvdf94@78!9"
        }
    },
    "invalid": {
        "user1": {
            "first_name": "*((*&",
            "last_name": "123",
            "email": "response@edu",
            "password": "103348494",
        }
    }
}

candidate_registration_form_data = {
    "valid": {
        "user1": {
            "first_name": "Jane",
            "last_name": "Jameson",
            "email": "jane@example.com",
            "password1": "cN3KJXi4GxsCxZET",
            "password2": "cN3KJXi4GxsCxZET",
        },
        "user2": {
            "first_name": "Alex",
            "last_name": "Rodriguez",
            "email": "username@gmail.com",
            "password1": "'LKlk#fvdf94@78!9",
            "password2": "'LKlk#fvdf94@78!9",
        },
    },
    "invalid": {
        "missing_first_name", {
            "first_name": "",
            "last_name": user_data["valid"]["user1"]["last_name"],
            "email": user_data["valid"]["user1"]["email"],
            "password1": user_data["valid"]["user1"]["password"],
            "password2": user_data["valid"]["user1"]["password"],
        },
        "missing_last_name", {
            "first_name": user_data["valid"]["user1"]["first_name"],
            "last_name": "",
            "email": user_data["valid"]["user1"]["email"],
            "password1": user_data["valid"]["user1"]["password"],
            "password2": user_data["valid"]["user1"]["password"],
        },
        "missing_email", {
            "first_name": user_data["valid"]["user1"]["first_name"],
            "last_name": user_data["valid"]["user1"]["last_name"],
            "email": "",
            "password1": user_data["valid"]["user1"]["password"],
            "password2": user_data["valid"]["user1"]["password"],
        },
        "missing_password1", {
            "first_name": user_data["valid"]["user1"]["first_name"],
            "last_name": user_data["valid"]["user1"]["last_name"],
            "email": user_data["valid"]["user1"]["email"],
            "password1": "",
            "password2": user_data["valid"]["user1"]["password"],
        },
        "missing_password2", {
            "first_name": user_data["valid"]["user1"]["first_name"],
            "last_name": user_data["valid"]["user1"]["last_name"],
            "email": user_data["valid"]["user1"]["email"],
            "password1": user_data["valid"]["user1"]["password"],
            "password2": "",
        },
        "password_mismatch", {
            "first_name": user_data["valid"]["user1"]["first_name"],
            "last_name": user_data["valid"]["user1"]["last_name"],
            "email": user_data["valid"]["user1"]["email"],
            "password1": user_data["valid"]["user1"]["password"],
            "password2": user_data["valid"]["user2"]["password"],
        },
        "first_name_invalid", {
            "first_name": user_data["invalid"]["user1"]["first_name"],
            "last_name": user_data["valid"]["user1"]["last_name"],
            "email": user_data["valid"]["user1"]["email"],
            "password1": user_data["valid"]["user1"]["password"],
            "password2": user_data["valid"]["user1"]["password"],
        },
        "last_name_invalid", {
            "first_name": user_data["valid"]["user1"]["first_name"],
            "last_name": user_data["invalid"]["user1"]["last_name"],
            "email": user_data["valid"]["user1"]["email"],
            "password1": user_data["valid"]["user1"]["password"],
            "password2": user_data["valid"]["user1"]["password"],
        },
        "email_invalid", {
            "first_name": user_data["valid"]["user1"]["first_name"],
            "last_name": user_data["valid"]["user1"]["last_name"],
            "email": user_data["invalid"]["user1"]["email"],
            "password1": user_data["valid"]["user1"]["password"],
            "password2": user_data["valid"]["user1"]["password"],
        },
        "password1_invalid", {
            "first_name": user_data["valid"]["user1"]["first_name"],
            "last_name": user_data["valid"]["user1"]["last_name"],
            "email": user_data["invalid"]["user1"]["email"],
            "password1": user_data["invalid"]["user1"]["password"],
            "password2": user_data["valid"]["user1"]["password"],
        },
        "password2_invalid", {
            "first_name": user_data["valid"]["user1"]["first_name"],
            "last_name": user_data["valid"]["user1"]["last_name"],
            "email": user_data["valid"]["user1"]["email"],
            "password1": user_data["valid"]["user1"]["password"],
            "password2": user_data["invalid"]["user1"]["password"],
        }
    }
}


def post_to_view(self, view, data):
    return self.client.post(reverse(view), data=data)


def create_department():
    return Department.objects.create(id=1, name="NYC Fire")

#Uses user_data["valid"]["user2"] - user2
def create_employer(department):
    cu = CustomUser.objects.create_user(
        email=user_data["valid"]["user2"]["email"],
        password=user_data["valid"]["user2"]["password"],
        first_name=user_data["valid"]["user2"]["first_name"],
        last_name=user_data["valid"]["user2"]["last_name"],
    )
    return Employer.objects.create(user=cu, department=department)

#Uses user_data["valid"]["user1"] - user1
def create_candidate():
    cu = CustomUser.objects.create_user(
        email=user_data["valid"]["user1"]["email"],
        password=user_data["valid"]["user1"]["password"],
        first_name=user_data["valid"]["user1"]["first_name"],
        last_name=user_data["valid"]["user1"]["last_name"],
        is_candidate=True,
    )
    profile = CandidateProfile.objects.create()
    return Candidate.objects.create(user=cu, candidate_profile=profile)

departments = {
    1: {
        "name": "NYC Fire",
    },
    2: {
        "name": "NYC Health",
    },
    3: {
        "name": "NYC Public Works",
    },
    4: {
        "name": "NYC Law",
    },
    5: {
        "name": "NYC Food",
    },
    6: {
        "name": "NYC Art",
    },
    7: {
        "name": "NYC Education",
    },
    8: {
        "name": "NYC Labor",
    },
    9: {
        "name": "NYC Tourism",
    },
    10: {
        "name": "NYC Agriculture",
    },
}

job_details = {
    "job_id": "87990",
    "department": 1,
    "posting_type": "Internal",
    "business_title": "Account Manager",
    "civil_service_title": "'CONTRACT REVIEWER (OFFICE OF L",
    "title_code_no": "40563",
    "level": "1",
    "job_category": "",
    "ft_pt_indicator": "",
    "salary_start": Decimal("42405.0000000000"),
    "salary_end": Decimal("65485.0000000000"),
    "salary_frequency": "Annual",
    "work_location": "110 William St. N Y",
    "division": "Strategy & Analytics",
    "job_description": "Some text.",
    "min_qualifications": "Quals",
    "preferred_skills": "skills",
    "additional_info": "",
    "to_apply": "apply",
    "hours_info": "some hours",
    "secondary_work_location": "Brooklyn, NY",
    "recruitment_contact": "",
    "residency_requirement": "some reqs",
    "posting_date": datetime.date(2015, 2, 19),
    "post_until": None,
    "posting_updated": datetime.date(2015, 2, 19),
    "process_date": datetime.date(2019, 10, 15),
}

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