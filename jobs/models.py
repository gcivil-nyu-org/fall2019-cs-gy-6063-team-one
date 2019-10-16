from django.db import models


# Create your models here.
class Job(models.Model):

    job_id = models.IntegerField(primary_key=True)
    agency = models.CharField(max_length=2000)
    posting_type = models.CharField(max_length=2000)
    business_title = models.CharField(max_length=2000)
    civil_service_title = models.CharField(max_length=2000)
    title_code_no = models.CharField(max_length=2000)
    level = models.CharField(max_length=2000)
    job_category = models.CharField(max_length=2000)
    ft_pt_indicator = models.CharField(max_length=2000)
    salary_start = models.DecimalField(max_digits=1000, decimal_places=10)
    salary_end = models.DecimalField(max_digits=1000, decimal_places=10)
    salary_frequency = models.CharField(max_length=2000)
    work_location = models.CharField(max_length=2000)
    division = models.CharField(max_length=2000)
    job_description = models.CharField(max_length=2000)
    min_qualifications = models.CharField(max_length=2000)
    preferred_skills = models.CharField(max_length=2000)
    additional_info = models.CharField(max_length=2000)
    to_apply = models.CharField(max_length=2000)
    hours_info = models.CharField(max_length=2000)
    secondary_work_location = models.CharField(max_length=2000)
    recruitment_contact = models.CharField(max_length=2000)
    residency_requirement = models.CharField(max_length=2000)
    posting_date = models.DateField(blank=True, null=True)
    post_until = models.DateField(blank=True, null=True)
    posting_updated = models.DateField(blank=True, null=True)
    process_date = models.DateField(blank=True, null=True)

