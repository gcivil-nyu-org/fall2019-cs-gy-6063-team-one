from django.db import models

MAX_CHARS = 12000


# Create your models here.
class Job(models.Model):
    job_id = models.IntegerField(primary_key=True)
    agency = models.CharField(max_length=MAX_CHARS)
    posting_type = models.CharField(max_length=MAX_CHARS)
    business_title = models.CharField(max_length=MAX_CHARS)
    civil_service_title = models.CharField(max_length=MAX_CHARS)
    title_code_no = models.CharField(max_length=MAX_CHARS)
    level = models.CharField(max_length=MAX_CHARS)
    job_category = models.CharField(max_length=MAX_CHARS)
    ft_pt_indicator = models.CharField(max_length=MAX_CHARS)
    salary_start = models.DecimalField(max_digits=1000, decimal_places=10)
    salary_end = models.DecimalField(max_digits=1000, decimal_places=10)
    salary_frequency = models.CharField(max_length=MAX_CHARS)
    work_location = models.CharField(max_length=MAX_CHARS)
    division = models.CharField(max_length=MAX_CHARS)
    job_description = models.CharField(max_length=MAX_CHARS)
    min_qualifications = models.CharField(max_length=MAX_CHARS)
    preferred_skills = models.CharField(max_length=MAX_CHARS)
    additional_info = models.CharField(max_length=MAX_CHARS)
    to_apply = models.CharField(max_length=MAX_CHARS)
    hours_info = models.CharField(max_length=MAX_CHARS)
    secondary_work_location = models.CharField(max_length=MAX_CHARS)
    recruitment_contact = models.CharField(max_length=MAX_CHARS)
    residency_requirement = models.CharField(max_length=MAX_CHARS)
    posting_date = models.DateField(blank=True, null=True)
    post_until = models.DateField(blank=True, null=True)
    posting_updated = models.DateField(blank=True, null=True)
    process_date = models.DateField(blank=True, null=True)

    def __eq__(self, other):
        return self.job_id == other.job_id

    def __ne__(self, other):
        return self.job_id != other.job_id


