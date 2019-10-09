from django import forms
from django.forms import ModelForm, ModelChoiceField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CandidateRegistrationForm(ModelForm):
    def __init__(self, *args, **kwargs): 
    	super(CandidateRegistrationForm, self).__init__(*args, **kwargs)
    	self.fields['password2'].label = 'Retype password'

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'username', 'password', 'password2')
        


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')