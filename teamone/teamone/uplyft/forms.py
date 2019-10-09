from django import forms
from django.forms import ModelForm, ModelChoiceField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CandidateRegistrationModel, CustomUser

class CandidateRegistrationForm(ModelForm):
    
    class Meta:
        model = CandidateRegistrationModel
        fields = '__all__'  

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')