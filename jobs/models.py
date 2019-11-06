from django.db import models

MAX_CHARS = 12000


class Department(models.Model):
    name = models.CharField(max_length=MAX_CHARS, unique=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    job_id = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
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
        if not other:
            return False
        return self.id == other.id

    def __ne__(self, other):
        if not other:
            return False
        return self.id != other.id


class SavedJobs(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    user = models.ForeignKey("uplyft.CustomUser", on_delete=models.CASCADE)