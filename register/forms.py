from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

from jobs.models import Department


class CandidateRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label="First Name", max_length=60, required=True)
    last_name = forms.CharField(label="Last Name", max_length=60, required=True)
    email = forms.EmailField(label="Email", max_length=200, required=True)

    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email")

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        users_with_email = get_user_model().objects.filter(email=email)
        if users_with_email.count() > 0:
            raise ValidationError("Email already exists")
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"].lower()
        if not first_name.isalpha():
            raise ValidationError("First name should contain only letters (A-Z).")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"].lower()
        if not last_name.isalpha():
            raise ValidationError("Last name should contain only letters (A-Z).")
        return last_name


class EmployerRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label="First Name", max_length=60, required=True)
    last_name = forms.CharField(label="Last Name", max_length=60, required=True)
    email = forms.EmailField(label="Email", max_length=200, required=True)
    department = forms.ModelChoiceField(queryset=Department.objects.all().order_by('name'))

    class Meta:
        model = get_user_model()
        fields = ("first_name", "last_name", "email")

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        users_with_email = get_user_model().objects.filter(email=email)
        if users_with_email.count() > 0:
            raise ValidationError("Email already exists")
        return email

    def clean_first_name(self):
        first_name = self.cleaned_data["first_name"].lower()
        if not first_name.isalpha():
            raise ValidationError("First name should contain only letters (A-Z).")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data["last_name"].lower()
        if not last_name.isalpha():
            raise ValidationError("Last name should contain only letters (A-Z).")
        return last_name

    def clean_department(self):
        department = self.cleaned_data["department"]
        if department == "":
            raise ValidationError("Please select a department.")
        return department
