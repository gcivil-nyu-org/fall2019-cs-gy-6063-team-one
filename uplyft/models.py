import datetime
from django.utils import timezone
from django import forms
from django.db import models
from django.forms import ModelForm, ModelChoiceField
from django.contrib.auth.models import AbstractUser

#https://django-localflavor.readthedocs.io/en/latest/localflavor/us/
from localflavor.us.models import USStateField, USZipCodeField

class CustomUser(AbstractUser):
    def __str__(self):
        return self.username
