import datetime
from django.utils import timezone
from django.db import models
from django.forms import ModelForm, ModelChoiceField
from django.contrib.auth.models import AbstractUser

#https://django-localflavor.readthedocs.io/en/latest/localflavor/us/
from localflavor.us.models import USStateField, USZipCodeField 

EMPLOYERS = [
    ('NYCZ', 'New York City Zoo'),
    ('NYCPD', 'New York City Police Department'),
]

OCCUPATIONS = [
    ('STUDENT', 'Student'), 
    ('FULL TIME', 'Full time employee'), 
    ('PART TIME', 'Part time employee'),
]

YEARS_OF_EXPERIENCE = [
    ('0-1', '0 to 1 year'),
    ('2', '2 years'),
    ('3-5', '3-5 years'),
    ('5-10', '5-10 years'), 
    ('10+', '10+ years'),
]

class User(AbstractUser):
    #TODO

class CandidateRegistrationModel(models.Model):
    first_name = models.CharField(
        max_length=60,
        null=False,
        blank=True,
        help_text="The candidate's first name.",
    )
    last_name = models.CharField(
        max_length=60,
        null=False,
        blank=True,
        help_text="The candidate's last name.",
    )
    email = models.EmailField(
        max_length=200,
        null=False,
        blank=True,
        help_text="The candidate's email address.",
    )
    password = models.CharField(
        max_length=200,
        null=False,
        blank=True,
        help_text="The candidate's password.",
    )
    password_retype = models.CharField(
        max_length=200,
        null=False,
        blank=True,
        help_text="The candidate's password, again.",
    )
    occupation = models.CharField(
        max_length=100,
        choices = OCCUPATIONS,
        null=False,
        #empty_label = "Pick an occupation type",
        help_text="The candidate's occupation.",
    )
    phone_number = models.CharField(
        null=False,
        #empty_label = "(212)-200-0000",
        max_length = 12, 
        help_text = "The candidate's phone number.",
        # @TODO https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
    )
    address_line_1 = models.CharField(
        null=True, 
        #empty_label = "Street, Building Number",
        max_length = 200, 
        help_text = "The candidate's address (line 1).",
    )
    address_line_2 = models.CharField(
        null=True, 
        #empty_label = "",
        max_length = 200, 
        help_text = "Apartment/Unit Number",
    )
    city = models.CharField(
        max_length = 200, 
        null = False,
        help_text = "The candidate's city.",
    )
    state = USStateField(
        null = False,
        help_text = "The candidate's state.",
    )
    zipcode = USZipCodeField(
        null=False, 
        help_text = "The candidate's zipcode.", 
    )
    skills = models.CharField( # Will need to become a dynamic number of text boxes
        max_length = 500, 
        null = False, 
        help_text = "The candidate's skills",
    )
    years_of_experience = models.CharField(
        max_length = 100, 
        choices = YEARS_OF_EXPERIENCE, 
        null = False, 
        help_text = "The candidate's number of years of employment experience.",
    )
    disability_form_upload = models.FileField(
        null = True, 
        max_length = 200, 
    )
    veteran_status_upload = models.FileField(
        null = True, 
        max_length = 200, 
    )
    resume_upload = models.FileField(
        null = True, 
        max_length = 200, 
    )
    photo_upload = models.FileField(
        null = True, 
        max_length = 200, 
    )

    def __str__(self):
        return self.first_name