from django import forms
from jobs.models import DepartmentProfile
from django.core.exceptions import ValidationError


class DepartmentProfileForm(forms.ModelForm):
    class Meta:
        model = DepartmentProfile
        fields = ("address", "description", "website", "phone", "email")
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'phone': forms.TextInput(attrs={'placeholder': 'e.g. +12125552368'})
        }

    def __init__(self, *args, **kwargs):
        super(DepartmentProfileForm, self).__init__(*args, **kwargs)
        self.fields["address"].required = False
        self.fields["description"].required = False
        self.fields["website"].required = False
        self.fields["phone"].required = False
        self.fields["email"].required = False

    def clean(self):
        super(DepartmentProfileForm, self).clean()
        # This method will set the `cleaned_data` attribute

        address = self.cleaned_data.get("address")
        description = self.cleaned_data.get("description")
        website = self.cleaned_data.get("website")
        phone = self.cleaned_data.get("phone")
        email = self.cleaned_data.get("email")

        # if address is None and description is None and website is None:
        # raise ValidationError("No changes requested - fill out the form!")

        address = (
            self.cleaned_data.get("address") if self.cleaned_data.get("address") else ""
        )
        description = (
            self.cleaned_data.get("description")
            if self.cleaned_data.get("description")
            else ""
        )
        website = (
            self.cleaned_data.get("website") if self.cleaned_data.get("website") else ""
        )
        phone = self.cleaned_data.get("phone") if self.cleaned_data.get("phone") else ""
        email = self.cleaned_data.get("email") if self.cleaned_data.get("email") else ""
        if (
            not address.strip()
            and not description.strip()
            and not website.strip()
            and not phone
            and not email.strip()
        ):
            raise ValidationError("No changes requested yet - fill out the form!")
