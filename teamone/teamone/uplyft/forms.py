from django import forms
from django.forms import ModelForm, ModelChoiceField
from .models import CandidateRegistrationModel

class CandidateRegistrationForm(ModelForm):
    class Meta:
        model = CandidateRegistrationModel
        fields = '__all__'  
        #exclude = [] 

"""
class CandidateRegistrationForm(forms.Form):
   	first_name = forms.

    name = forms.CharField(max_length=100)
    title = forms.CharField(
        max_length=3,
        widget=forms.Select(choices=TITLE_CHOICES),
    )
    birth_date = forms.DateField(required=False)
"""
