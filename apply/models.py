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
    ETHNICITY_HISPANIC_LATINO = "HL"
    ETHNICITY_OTHER = "OT"
    RACE_AMERICAN_INDIAN_ALASKA_NATIVE = "NATIVE"
    RACE_ASIAN = "ASIAN"
    RACE_BLACK_AFRICA = "BLACK"
    RACE_NATIVE_HAWAIIAN_PACIFIC_ISLANDER = "PACIFIC"
    RACE_WHITE = "WHITE"
    DISABILITY_HEALTH_CONDITIONS_POSITIVE = "POSITIVE"
    DISABILITY_HEALTH_CONDITIONS_NEGATIVE = "NEGATIVE"
    VETERAN_POSITIVE = "POSITIVE"
    VETERAN_NEGATIVE = "NEGATIVE"
    DEMOGRAPHIC_CHOICES = [
        (
            "Gender",
            (
                (GENDER_CHOICE_FEMALE, "Female"),
                (GENDER_CHOICE_MALE, "Male"),
                (GENDER_CHOICE_NON_BINARY, "Non Binary"),
            ),
        ),
        (
            "Ethnicity",
            (
                (ETHNICITY_HISPANIC_LATINO, "Hispanic or Latino"),
                (ETHNICITY_OTHER, "Not Hispanic or Latino"),
                (None, "Prefer not to specify"),
            ),
        ),
        (
            "Race",
            (
                (
                    RACE_AMERICAN_INDIAN_ALASKA_NATIVE,
                    "American indian or Alaska Native",
                ),
                (RACE_ASIAN, "Asian"),
                (RACE_BLACK_AFRICA, "Black or African American"),
                (
                    RACE_NATIVE_HAWAIIAN_PACIFIC_ISLANDER,
                    "Native Hawaiian or Pacific Islander",
                ),
                (RACE_WHITE, "White"),
                (None, "Prefer not to specify"),
            ),
        ),
        (
            "Disability and Health Conditions",
            (
                (
                    DISABILITY_HEALTH_CONDITIONS_POSITIVE,
                    "One or more health conditions",
                ),
                (DISABILITY_HEALTH_CONDITIONS_NEGATIVE, "None listed apply"),
                (None, "Prefer not to specify"),
            ),
        ),
        (
            "Veteran",
            (
                (VETERAN_POSITIVE, "Veteran"),
                (VETERAN_NEGATIVE, "Not veteran"),
                (None, "Prefer not to specify"),
            ),
        ),
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=DEMOGRAPHIC_CHOICES[0][1])
    ethnicity = models.CharField(max_length=2, choices=DEMOGRAPHIC_CHOICES[1][1])
    race = models.CharField(max_length=7, choices=DEMOGRAPHIC_CHOICES[2][1])
    health_conditions = models.CharField(
        max_length=8, choices=DEMOGRAPHIC_CHOICES[3][1]
    )
    veteran = models.CharField(max_length=8, choices=DEMOGRAPHIC_CHOICES[4][1])
    address_line = models.CharField(max_length=100)
    zip_code = mailing.USZipCodeField()
    state = mailing.USStateField()
    phone = PhoneField()
    email = models.EmailField()
    porfolio_website = models.URLField(help_text="Maximum 200 characters")
    # Cover Letter
    cover_letter = models.TextField(max_length=10000)
    # Resume chunks
    experiences = models.TextField(max_length=10000)
    education = models.TextField(max_length=10000)
    additional_info = models.TextField(max_length=10000, blank=True)
