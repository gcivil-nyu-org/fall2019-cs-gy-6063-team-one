from django.db import models
from datetime import datetime
from jobs.models import Job
from uplyft.models import CandidateProfile, Candidate

MAX_EMAIL_LENGTH = 60


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    submit_date = models.DateField(null=False, default=datetime.now)
    STATUS_APPLIED = "AP"
    STATUS_ACCEPTED = "AC"
    STATUS_REJECTED = "RE"
    STATUS_CHOICES = [
        (STATUS_APPLIED, "Applied"),
        (STATUS_ACCEPTED, "Accepted"),
        (STATUS_REJECTED, "Rejected"),
    ]
    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES, default=STATUS_APPLIED
    )
    candidate_profile = models.OneToOneField(CandidateProfile, on_delete=models.CASCADE)
