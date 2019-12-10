from uplyft.models import CustomUser
from jobs.models import Job, Department, DepartmentProfile
from apply.models import Application
from uplyft.models import Candidate, Employer, CandidateProfile, ActiveProfile
import datetime
from decimal import Decimal
from django.core.files.uploadedfile import SimpleUploadedFile


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
            "resume": SimpleUploadedFile(
                "test_resume_0.pdf",
                open("media/tests/test_resume_0.pdf", "rb").read(),
                content_type="application/pdf",
            ),
            "cover_letter": SimpleUploadedFile(
                "test_cover_letter_0.pdf",
                open("media/tests/test_cover_letter_0.pdf", "rb").read(),
                content_type="application/pdf",
            ),
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
            "phone": "+12013348135",
            "portfolio_website": "https://janeTjameson.com",
            "resume": SimpleUploadedFile(
                "test_resume1.pdf",
                open("media/tests/test_resume_1.pdf", "rb").read(),
                content_type="application/pdf",
            ),
            "cover_letter": SimpleUploadedFile(
                "test_cover_letter_1.pdf",
                open("media/tests/test_cover_letter_1.pdf", "rb").read(),
                content_type="application/pdf",
            ),
            "additional_info": "Good at art",
        },
    },
    "candidates": [
        {
            "first_name": "Jane",
            "last_name": "Jameson",
            "email": "jane9@example.com",
            "password": "cN3KJXi4GxsCxZET",
            "password1": "cN3KJXi4GxsCxZET",
            "password2": "cN3KJXi4GxsCxZET",
            "profile": {
                "first_name": "Jane",
                "last_name": "Jameson",
                "email": "jane30@example.com",
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
                "resume": SimpleUploadedFile(
                    "test_resume_2.pdf",
                    open("media/tests/test_resume_2.pdf", "rb").read(),
                    content_type="application/pdf",
                ),
                "cover_letter": SimpleUploadedFile(
                    "test_cover_letter_2.pdf",
                    open("media/tests/test_cover_letter_2.pdf", "rb").read(),
                    content_type="application/pdf",
                ),
                "additional_info": "Good listener",
            },
        },
        {
            "first_name": "Michael",
            "last_name": "Scott",
            "email": "ms@michael.com",
            "password": "HappyBirthday2Me",
            "password1": "HappyBirthday2Me",
            "password2": "HappyBirthday2Me",
            "profile": {
                "first_name": "James",
                "last_name": "Bond",
                "email": "bond@edu.com",
                "gender": "M",
                "gender_display": "Male",
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
                "portfolio_website": "https://facebook.com",
                "resume": SimpleUploadedFile(
                    "test_resume_3.pdf",
                    open("media/tests/test_resume_3.pdf", "rb").read(),
                    content_type="application/pdf",
                ),
                "cover_letter": SimpleUploadedFile(
                    "test_cover_letter_3.pdf",
                    open("media/tests/test_cover_letter_3.pdf", "rb").read(),
                    content_type="application/pdf",
                ),
                "additional_info": "Good listener",
            },
        },
        {
            "first_name": "James",
            "last_name": "Michael Michaels",
            "email": "mms@michael.com",
            "password": "HappyBirthday2You",
            "password1": "HappyBirthday2You",
            "password2": "HappyBirthday2You",
            "profile": {
                "first_name": "Jimmy",
                "last_name": "The Tank",
                "email": "tj@yahoo.edu.com",
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
                "address_line": "112 W. 14th Street #4D",
                "zip_code": "10012",
                "state": "NY",
                "state_display": "New York",
                "phone": "+12018347135",
                "portfolio_website": "https://facebook2.com",
                "resume": SimpleUploadedFile(
                    "test_resume_4.pdf",
                    open("media/tests/test_resume_4.pdf", "rb").read(),
                    content_type="application/pdf",
                ),
                "cover_letter": SimpleUploadedFile(
                    "test_cover_letter_4.pdf",
                    open("media/tests/test_cover_letter_4.pdf", "rb").read(),
                    content_type="application/pdf",
                ),
                "additional_info": "Special kind of guy",
            },
        },
    ],
    "employer": {
        "first_name": "John",
        "last_name": "Johnson",
        "email": "john@example.com",
        "password": "cN3KJXi35374GxsCxZET",
        "password1": "cN3KJXi35374GxsCxZET",
        "password2": "cN3KJXi35374GxsCxZET",
    },
    "employers": [
        {
            "first_name": "John",
            "last_name": "Johnson",
            "email": "john@example.com",
            "password": "cN3KJXi35374GxsCxZET",
            "password1": "cN3KJXi35374GxsCxZET",
            "password2": "cN3KJXi35374GxsCxZET",
        },
        {
            "first_name": "James",
            "last_name": "JoJohnson",
            "email": "john@goooooogle.com",
            "password": "cN3KJXi35374GxsCxZET",
            "password1": "cN3KJXi35374GxsCxZET",
            "password2": "cN3KJXi35374GxsCxZET",
        },
    ],
    "invalid_user_details": {
        "first_name": "...",
        "last_name": "***()()",
        "email": "response@edu",
        "password": "103348494",
    },
    "department": {
        "id": 1,
        "name": "NYC Fire",
        "department_profile": {
            "description": "We stop fires.",
            "website": "https://fires.com",
            "address": "113 Broadway, New York NY 10012",
            "phone": "+12129471135",
            "email": "firedept@nyu.gov",
        },
    },
    "departments": [
        {
            "id": 1,
            "name": "NYC Fire",
            "department_profile": {
                "description": "We stop fires.",
                "website": "https://fires.com",
                "address": "113 Broadway, New York NY 10012",
                "phone": "+12129471135",
                "email": "firedept@nyc.gov",
            },
        },
        {
            "id": 2,
            "name": "NYC Health",
            "department_profile": {
                "description": "We stop diseases.",
                "website": "https://healthnyc.com",
                "address": "113 Broadway, New York NY 10012",
                "phone": "+2013347193",
                "email": "health@nyc.gov",
            },
        },
    ],
    "department_with_no_profile": {
        "id": 2,
        "name": "NYC Water",
        "department_profile": {},
    },
    "job_details": [
        {
            "id": 87990,
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
            "id": 87991,
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
        id=job_details["id"],
        department=department,
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


def create_user(user_data, is_candidate, is_active):
    return CustomUser.objects.create_user(
        email=user_data["email"],
        password=user_data["password"],
        first_name=user_data["first_name"],
        last_name=user_data["last_name"],
        is_candidate=is_candidate,
        is_active=is_active,
    )


def create_candidate_with_active_profile(user_data):
    custom_user = CustomUser.objects.create_user(
        email=user_data["email"],
        password=user_data["password"],
        first_name=user_data["first_name"],
        last_name=user_data["last_name"],
        is_candidate=True,
        is_active=True,
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
        resume=user_data["profile"]["resume"],
        cover_letter=user_data["profile"]["cover_letter"],
        additional_info=user_data["profile"]["additional_info"],
    )
    candidate = Candidate.objects.create(user=custom_user, candidate_profile=profile)
    ActiveProfile.objects.create(candidate=candidate, candidate_profile=profile)
    return candidate


def create_department(data):
    return Department.objects.create(id=data["id"], name=data["name"])


def create_department_with_profile(data):
    profile = DepartmentProfile.objects.create(
        address=data["department_profile"]["address"],
        description=data["department_profile"]["description"],
        website=data["department_profile"]["website"],
        phone=data["department_profile"]["phone"],
        email=data["department_profile"]["email"],
    )

    return Department.objects.create(
        id=data["id"], name=data["name"], department_profile=profile
    )


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
        resume=user_data["resume"],
        cover_letter=user_data["cover_letter"],
        additional_info=user_data["additional_info"],
    )


def create_application(job, candidate, profile):
    return Application.objects.create(
        job=job, candidate=candidate, candidate_profile=profile
    )
