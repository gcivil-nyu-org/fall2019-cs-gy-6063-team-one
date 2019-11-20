from django import forms
from jobs.models import DepartmentProfile


class DepartmentProfileForm(forms.ModelForm):
    class Meta:
        model = DepartmentProfile
        fields = ("address", "description", "website")

    def __init__(self, *args, **kwargs):
        super(DepartmentProfileForm, self).__init__(*args, **kwargs)
        self.fields["address"].required = False
        self.fields["description"].required = False
        self.fields["website"].required = False
