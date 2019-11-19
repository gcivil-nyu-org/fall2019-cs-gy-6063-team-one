from django import forms
from jobs.models import DepartmentProfile


class DepartmentProfileForm(forms.ModelForm):
    class Meta:
        model = DepartmentProfile
        fields = ("address", "description", "website", "photo_upload")

    def __init__(self, *args, **kwargs):
        super(DepartmentProfileForm, self).__init__(*args, **kwargs)
        self.fields["address"].required = False
        self.fields["description"].required = False
        self.fields["website"].required = False
        self.fields["photo_upload"].required = False
