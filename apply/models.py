from django.db import models
from datetime import datetime
from jobs.models import Job
from django.contrib.auth import get_user_model
from phone_field import PhoneField
from localflavor.us import models as mailing

MAX_EMAIL_LENGTH = 60


class Application(models.Model):
    # Meta
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    candidate = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
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
    # Demographic
    GENDER_CHOICE_FEMALE = "F"
    GENDER_CHOICE_MALE = "M"
    GENDER_CHOICE_NON_BINARY = "X"
    DEMOGRAPHIC_CHOICES = [
        (
            "Gender",
            (
                (GENDER_CHOICE_FEMALE, "Female"),
                (GENDER_CHOICE_MALE, "Male"),
                (GENDER_CHOICE_NON_BINARY, "Non Binary"),
            ),
        )
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=DEMOGRAPHIC_CHOICES[0][1])
    address_line = models.CharField(max_length=100)
    zip_code = mailing.USZipCodeField()
    state = mailing.USStateField()
    phone = PhoneField()
    email = models.EmailField()
    porfolio_website = models.URLField(help_text="Maximum 200 characters")
    # TODO: compliance related demographic questions
    # Cover Letter
    cover_letter = models.TextField(max_length=10000)
    # Resume chunks
    experiences = models.TextField(max_length=10000)
    education = models.TextField(max_length=10000)
    additional_info = models.TextField(max_length=10000, blank=True)
