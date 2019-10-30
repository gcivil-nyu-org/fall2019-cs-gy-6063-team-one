from django.db import models
from datetime import datetime
from jobs.models import Job
from django.contrib.auth import get_user_model

MAX_EMAIL_LENGTH = 60


class Application(models.Model):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    candidate = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    submit_date = models.DateField(null=False, default=datetime.now)
    STATUS_CHOICES = [(ACTIVE, "ACTIVE"), (INACTIVE, "INACTIVE")]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=ACTIVE)
