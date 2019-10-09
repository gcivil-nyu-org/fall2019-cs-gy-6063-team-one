from django import forms
from django.forms import ModelForm, ModelChoiceField
from .models import CandidateRegistrationModel

class CandidateRegistrationForm(ModelForm):
    class Meta:
        model = CandidateRegistrationModel
        fields = '__all__'  