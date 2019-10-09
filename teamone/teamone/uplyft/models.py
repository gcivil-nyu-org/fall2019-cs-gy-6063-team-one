import datetime
from django.utils import timezone
from django import forms
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

class CustomUser(AbstractUser):
    def __str__(self):
        return self.username
