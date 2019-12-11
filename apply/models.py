from django.db import models

from jobs.models import Job
from uplyft.models import CandidateProfile, Candidate

MAX_EMAIL_LENGTH = 60


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    submit_date = models.DateField(auto_now_add=True, null=False)
    STATUS_APPLIED = "AP"
    STATUS_ACCEPTED = "AC"
    STATUS_REJECTED = "RE"
    STATUS_WITHDRAWN = "W"
    STATUS_CHOICES = [
        (STATUS_APPLIED, "Applied"),
        (STATUS_ACCEPTED, "Accepted"),
        (STATUS_REJECTED, "Rejected"),
        (STATUS_WITHDRAWN, "Withdrawn"),
    ]
    status = models.CharField(
        max_length=2, choices=STATUS_CHOICES, default=STATUS_APPLIED
    )
    candidate_profile = models.ForeignKey(
        CandidateProfile, on_delete=models.CASCADE, null=True
    )
