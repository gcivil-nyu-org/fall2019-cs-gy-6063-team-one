from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class UplyftCandidateLoginForm(AuthenticationForm):
    foo = 'hello'

    class Meta:
        model = get_user_model()
        # fields = CustomUserCreationForm.Meta.fields

