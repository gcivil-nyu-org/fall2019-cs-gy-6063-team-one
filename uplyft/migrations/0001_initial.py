# Generated by Django 2.2.6 on 2019-11-18 21:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import localflavor.us.models
import phonenumber_field.modelfields
import uplyft.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("auth", "0011_update_proxy_permissions"), ("jobs", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions "
                        "without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=30, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this "
                        "admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as "
                        "active. Unselect this instead of deleting "
                        "accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="email address"
                    ),
                ),
                ("is_candidate", models.BooleanField(default=False)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get "
                        "all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[("objects", uplyft.models.CustomUserManager())],
        ),
        migrations.CreateModel(
            name="CandidateProfile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=30, null=True)),
                ("last_name", models.CharField(blank=True, max_length=30, null=True)),
                (
                    "gender",
                    models.CharField(
                        blank=True,
                        choices=[("F", "Female"), ("M", "Male"), ("X", "Non Binary")],
                        max_length=1,
                        null=True,
                    ),
                ),
                (
                    "ethnicity",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("HL", "Hispanic or Latino"),
                            ("OT", "Not Hispanic or Latino"),
                            (None, "Prefer not to specify"),
                        ],
                        max_length=2,
                        null=True,
                    ),
                ),
                (
                    "race",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("NATIVE", "American indian or Alaska Native"),
                            ("ASIAN", "Asian"),
                            ("BLACK", "Black or African American"),
                            ("PACIFIC", "Native Hawaiian or Pacific Islander"),
                            ("WHITE", "White"),
                            (None, "Prefer not to specify"),
                        ],
                        max_length=7,
                        null=True,
                    ),
                ),
                (
                    "health_conditions",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("POSITIVE", "One or more health conditions"),
                            ("NEGATIVE", "None listed apply"),
                            (None, "Prefer not to specify"),
                        ],
                        max_length=8,
                        null=True,
                    ),
                ),
                (
                    "veteran",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("POSITIVE", "Veteran"),
                            ("NEGATIVE", "Not veteran"),
                            (None, "Prefer not to specify"),
                        ],
                        max_length=8,
                        null=True,
                    ),
                ),
                (
                    "address_line",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "zip_code",
                    localflavor.us.models.USZipCodeField(
                        blank=True, max_length=10, null=True
                    ),
                ),
                (
                    "state",
                    localflavor.us.models.USStateField(
                        blank=True, max_length=2, null=True
                    ),
                ),
                (
                    "phone",
                    phonenumber_field.modelfields.PhoneNumberField(
                        blank=True, max_length=128, null=True, region=None
                    ),
                ),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                (
                    "portfolio_website",
                    models.URLField(
                        blank=True, help_text="Maximum 200 characters", null=True
                    ),
                ),
                (
                    "cover_letter",
                    models.TextField(blank=True, max_length=10000, null=True),
                ),
                (
                    "experiences",
                    models.TextField(blank=True, max_length=10000, null=True),
                ),
                (
                    "education",
                    models.TextField(blank=True, max_length=10000, null=True),
                ),
                (
                    "additional_info",
                    models.TextField(blank=True, max_length=10000, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Employer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "department",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="jobs.Department",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Candidate",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "candidate_profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="uplyft.CandidateProfile",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ActiveProfile",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "candidate",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="uplyft.Candidate",
                    ),
                ),
                (
                    "candidate_profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="uplyft.CandidateProfile",
                    ),
                ),
            ],
        ),
    ]
