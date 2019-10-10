from django import forms
from django.forms import ModelForm, ModelChoiceField
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class CandidateRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    email = forms.EmailField(label="Email")

    class Meta: 
        model = get_user_model()
        fields = ("first_name", "last_name", "email",)

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        usersWithEmail = get_user_model().objects.filter(email=email)
        if usersWithEmail.count() > 0:
            raise ValidationError("Email already exists")
        return email


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('email',)