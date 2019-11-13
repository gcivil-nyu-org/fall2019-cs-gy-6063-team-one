from uplyft.models import CustomUser
from jobs.models import Job, Department
from apply.models import Application
from uplyft.models import Candidate, Employer, CandidateProfile, ActiveProfile
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
            "gender": "F",
            "gender_display": "Female",
            "ethnicity": "OT",
            "ethnicity_display": "Not Hispanic or Latino",
            "race": "ASIAN",
            "race_display": "Asian",
            "health_conditions": "POSITIVE",
            "health_conditions_display": "One or more health conditions",
            "veteran": "POSITIVE",
            "veteran_display": "Veteran",
            "address_line": "123 Main Street, Hoboken",
            "zip_code": "07030",
            "state": "NJ",
            "state_display": "New Jersey",
            "phone": "+12018347135",
            "portfolio_website": "https://janejameson.com",
            "cover_letter": "Please hire me, I need this job",
            "experiences": "Nada",
            "education": "Self-taught",
            "additional_info": "Good listener",
        },
        "new_profile": {
            "first_name": "Jaime",
            "last_name": "Jaimeson",
            "email": "jane1@example.com",
            "gender": "X",
            "gender_display": "Non Binary",
            "ethnicity": "HL",
            "ethnicity_display": "Hispanic or Latino",
            "race": "WHITE",
            "race_display": "White",
            "health_conditions": "NEGATIVE",
            "health_conditions_display": "None listed apply",
            "veteran": "NEGATIVE",
            "veteran_display": "Not veteran",
            "address_line": "1620 Manhattan Ave, Union City",
            "zip_code": "07087",
            "state": "NY",
            "state_display": "New York",
            "phone": "2013348135",
            "portfolio_website": "https://janeTjameson.com",
            "cover_letter": "Please hire me, I need this job. "
            "Since I wrote the original cover "
            "letter, nothing has changed...",
            "experiences": "Less than nada",
            "education": "Teach me?",
            "additional_info": "Good at art",
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
    "job_details": [
        {
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
        {
            "job_id": "87991",
            "posting_type": "Internal",
            "business_title": "Account Auditor",
            "civil_service_title": "Account Auditor",
            "title_code_no": "28907",
            "level": "0",
            "job_category": "",
            "ft_pt_indicator": "",
            "salary_start": Decimal("100000.0000000000"),
            "salary_end": Decimal("200000.0000000000"),
            "salary_frequency": "Annual",
            "work_location": "222 Broadway #32b N Y",
            "division": "Auditing",
            "job_description": "Some text.",
            "min_qualifications": "BA/MA Accounting Fordham 1998",
            "preferred_skills": "Maths",
            "additional_info": "Need to work from home in Massachussetts...",
            "to_apply": "apply",
            "hours_info": "9-5, 24/5",
            "secondary_work_location": "Brooklyn, NY",
            "recruitment_contact": "",
            "residency_requirement": "some reqs",
            "posting_date": datetime.date(2018, 2, 19),
            "post_until": None,
            "posting_updated": datetime.date(2018, 2, 19),
            "process_date": datetime.date(2019, 10, 15),
        },
    ],
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


def create_user(user_data, is_candidate):
    return CustomUser.objects.create_user(
        email=user_data["email"],
        password=user_data["password"],
        first_name=user_data["first_name"],
        last_name=user_data["last_name"],
        is_candidate=is_candidate,
    )


def create_candidate_with_active_profile(user_data):
    custom_user = CustomUser.objects.create_user(
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
        gender=user_data["profile"]["gender"],
        ethnicity=user_data["profile"]["ethnicity"],
        race=user_data["profile"]["race"],
        health_conditions=user_data["profile"]["health_conditions"],
        veteran=user_data["profile"]["veteran"],
        address_line=user_data["profile"]["address_line"],
        zip_code=user_data["profile"]["zip_code"],
        state=user_data["profile"]["state"],
        phone=user_data["profile"]["phone"],
        portfolio_website=user_data["profile"]["portfolio_website"],
        cover_letter=user_data["profile"]["cover_letter"],
        experiences=user_data["profile"]["experiences"],
        education=user_data["profile"]["education"],
        additional_info=user_data["profile"]["additional_info"],
    )
    candidate = Candidate.objects.create(user=custom_user, candidate_profile=profile)
    ActiveProfile.objects.create(candidate=candidate, candidate_profile=profile)
    return candidate


def create_profile(user_data):
    return CandidateProfile.objects.create(
        email=user_data["email"],
        first_name=user_data["first_name"],
        last_name=user_data["last_name"],
        gender=user_data["gender"],
        ethnicity=user_data["ethnicity"],
        race=user_data["race"],
        health_conditions=user_data["health_conditions"],
        veteran=user_data["veteran"],
        address_line=user_data["address_line"],
        zip_code=user_data["zip_code"],
        state=user_data["state"],
        phone=user_data["phone"],
        portfolio_website=user_data["portfolio_website"],
        cover_letter=user_data["cover_letter"],
        experiences=user_data["experiences"],
        education=user_data["education"],
        additional_info=user_data["additional_info"],
    )


def create_application(job, candidate, profile):
    return Application.objects.create(
        job=job, candidate=candidate, candidate_profile=profile
    )
