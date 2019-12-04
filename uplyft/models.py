from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from localflavor.us import models as mailing
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import FileExtensionValidator
from uuid_upload_path import upload_to
from django.core.exceptions import ValidationError

from jobs.models import Department
from uplyft.s3_storage import ResumeStorage


class CustomUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email is empty")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    is_candidate = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


def file_size(value):
    limit = 2 * 1024 * 1024
    if value.size > limit:
        raise ValidationError("File too large. Size should not exceed 2 MB")


class CandidateProfile(models.Model):
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
    first_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30, blank=True, null=True)
    gender = models.CharField(
        max_length=1, choices=DEMOGRAPHIC_CHOICES[0][1], blank=True, null=True
    )
    ethnicity = models.CharField(
        max_length=2, choices=DEMOGRAPHIC_CHOICES[1][1], blank=True, null=True
    )
    race = models.CharField(
        max_length=7, choices=DEMOGRAPHIC_CHOICES[2][1], blank=True, null=True
    )
    health_conditions = models.CharField(
        max_length=8, choices=DEMOGRAPHIC_CHOICES[3][1], blank=True, null=True
    )
    veteran = models.CharField(
        max_length=8, choices=DEMOGRAPHIC_CHOICES[4][1], blank=True, null=True
    )
    address_line = models.CharField(max_length=100, blank=True, null=True)
    zip_code = mailing.USZipCodeField(blank=True, null=True)
    state = mailing.USStateField(blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    portfolio_website = models.URLField(
        help_text="e.g. http://example.com", blank=True, null=True, max_length=200
    )
    # Cover Letter
    cover_letter = models.FileField(
        upload_to=upload_to,
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["pdf", "doc", "docx"]),
            file_size,
        ],
    )
    # Resume chunks
    resume = models.FileField(
        storage=ResumeStorage(),
        upload_to=upload_to,
        null=True,
        blank=True,
        validators=[
            FileExtensionValidator(allowed_extensions=["pdf", "doc", "docx"]),
            file_size,
        ],
    )
    additional_info = models.TextField(max_length=10000, blank=True, null=True)

    def __eq__(self, other):
        if not other:
            return False
        return self.id == other.id

    def __ne__(self, other):
        if not other:
            return False
        return self.id != other.id


class Candidate(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=False)
    candidate_profile = models.ForeignKey(
        CandidateProfile, on_delete=models.CASCADE, null=False
    )

    def __eq__(self, other):
        if not other:
            return False
        return self.id == other.id

    def __ne__(self, other):
        if not other:
            return False
        return self.id != other.id

    def __hash__(self):
        return self.user.__hash__()


class Employer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=False)

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return self.id != other.id


class ActiveProfile(models.Model):
    # This is effectively the same as having a foreign key with unique=True
    # To ensure each ActiveProfile belongs to only one candidate
    # and also that each candidate can have only one Active Profile
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    candidate_profile = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE)

    def __str__(self):
        string = "User ID: " + str(self.candidate.user_id)
        string += "; Candidate ID: " + str(self.candidate.id)
        string += "; Profile ID: " + str(self.candidate_profile.id)
