from uplyft.models import CustomUser
from jobs.models import Job, Department
from apply.models import Application
from uplyft.models import Candidate, Employer, CandidateProfile
import datetime
from decimal import Decimal

test_user_data = {
    "candidate": {
        "first_name": "Jane",
        "last_name": "Jameson",
        "email": "jane@example.com",
        "password": "cN3KJXi4GxsCxZET",
        "password1": "cN3KJXi4GxsCxZET",
        "password2": "cN3KJXi4GxsCxZET",
        "profile": {
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
        },
    },
    "employer": {
        "first_name": "John",
        "last_name": "Johnson",
        "email": "john@example.com",
        "password": "cN3KJXi35374GxsCxZET",
        "password1": "cN3KJXi35374GxsCxZET",
        "password2": "cN3KJXi35374GxsCxZET",
    },
    "invalid_user_details": {
        "first_name": "...",
        "last_name": "***()()",
        "email": "response@edu",
        "password": "103348494",
    },
    "department": {"id": 1, "name": "NYC Fire"},
    "job_details": {
        "job_id": "87990",
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
    },
}


def create_department(department):
    return Department.objects.create(id=department["id"], name=department["name"])


def create_employer(department, user_data):
    cu = CustomUser.objects.create_user(
        email=user_data["email"],
        password=user_data["password"],
        first_name=user_data["first_name"],
        last_name=user_data["last_name"],
        is_candidate=False,
    )
    return Employer.objects.create(user=cu, department=department)


def create_candidate(user_data):
    cu = CustomUser.objects.create_user(
        email=user_data["email"],
        password=user_data["password"],
        first_name=user_data["first_name"],
        last_name=user_data["last_name"],
        is_candidate=True,
    )
    profile = CandidateProfile.objects.create(
        email=user_data["email"],
        first_name=user_data["first_name"],
        last_name=user_data["last_name"],
    )
    return Candidate.objects.create(user=cu, candidate_profile=profile)


def create_job(department, job_details):
    return Job.objects.create(
        job_id=job_details["job_id"],
        department=department,
        posting_type=job_details["posting_type"],
        business_title=job_details["business_title"],
        civil_service_title=job_details["civil_service_title"],
        title_code_no=job_details["title_code_no"],
        level=job_details["level"],
        job_category=job_details["job_category"],
        ft_pt_indicator=job_details["ft_pt_indicator"],
        salary_start=job_details["salary_start"],
        salary_end=job_details["salary_end"],
        salary_frequency=job_details["salary_frequency"],
        work_location=job_details["work_location"],
        division=job_details["division"],
        job_description=job_details["job_description"],
        min_qualifications=job_details["min_qualifications"],
        preferred_skills=job_details["preferred_skills"],
        additional_info=job_details["additional_info"],
        to_apply=job_details["to_apply"],
        hours_info=job_details["hours_info"],
        secondary_work_location=job_details["secondary_work_location"],
        recruitment_contact=job_details["recruitment_contact"],
        residency_requirement=job_details["residency_requirement"],
        posting_date=job_details["posting_date"],
        post_until=job_details["post_until"],
        posting_updated=job_details["posting_updated"],
        process_date=job_details["process_date"],
    )


def create_application(job, candidate):
    return Application.objects.create(job=job, candidate=candidate)
