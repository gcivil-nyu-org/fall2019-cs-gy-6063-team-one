import logging
from datetime import datetime

import pandas
from numpy import NaN

from jobs.models import Department, Job

jobs_csv = pandas.read_csv("jobs/NYC_Jobs.csv", delimiter=",", encoding="UTF-8")
logger = logging.getLogger(__name__)


def create_departments():
    departments = set()
    for index, row in jobs_csv.iterrows():
        departments.add(row[1])
    for department in departments:
        save_department(department)


def save_department(department):
    db_department, created = Department.objects.get_or_create(name=department)
    if not created:
        logger.info("Department :{}: already exists, not updating".format(department))


def create_jobs():
    for index, row in jobs_csv.iterrows():
        for j, field in enumerate(row):
            # All columns after 22 are date fields, so if pandas reads it as NaN,
            # set to None
            if j > 22 and row[j] is NaN:
                row[j] = None
                continue
            # Column 24 has a different format compared to the other date columns.
            # This input is in the format %Y-%m-%dT%H:%M:%S.%f
            if j == 24:
                row[j] = datetime.strptime(row[j], "%Y-%m-%dT%H:%M:%S.%f").strftime(
                    "%Y-%m-%d"
                )
                continue
            # Any columns above 22 are date fields, and have the format %m/%d/%Y, only
            # for column 24, it is different, and its handled before this
            if j > 22:
                row[j] = datetime.strptime(row[j], "%m/%d/%Y").strftime("%Y-%m-%d")
        save_job(row)


def save_job(row):
    # row[1] contains the agency/department name
    department_name = row[1]
    department = Department.objects.get(name=department_name)
    job = Job(
        job_id=row[0],
        department=department,
        posting_type=row[2],
        business_title=row[3],
        civil_service_title=row[4],
        title_code_no=row[5],
        level=row[6],
        job_category=row[7],
        ft_pt_indicator=row[8],
        salary_start=row[9],
        salary_end=row[10],
        salary_frequency=row[11],
        work_location=row[12],
        division=row[13],
        job_description=row[14],
        min_qualifications=row[15],
        preferred_skills=row[16],
        additional_info=row[17],
        to_apply=row[18],
        hours_info=row[19],
        secondary_work_location=row[20],
        recruitment_contact=row[21],
        residency_requirement=row[22],
        posting_date=row[23],
        post_until=row[24],
        posting_updated=row[25],
        process_date=row[26],
    )
    job.save()
