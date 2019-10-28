from django.db import models
from datetime import datetime
from jobs.models import Job
from django.contrib.auth import get_user_model

MAX_EMAIL_LENGTH = 60


class Application(models.Model):
    SUBMITTED = "SUBMITTED"
    REVIEWED = "REVIEWED"
    INCOMPLETE = "INCOMPLETE"
    WITHDRAWN = "WITHDRAWN"
    app_id = models.IntegerField(primary_key=True)
    job_id = models.ForeignKey(Job, on_delete=models.CASCADE)
    candidate = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    submit_date = models.DateField(null=False, default=datetime.now)
    STATUS_CHOICES = [
        (SUBMITTED, "Submitted"),
        (REVIEWED, "Reviewed"),
        (INCOMPLETE, "Incomplete"),
        (WITHDRAWN, "Withdrawn"),
    ]
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=SUBMITTED,
    )

    def __str__(self):
        return self.app_id