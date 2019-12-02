import django_filters
from django_select2 import forms as select2_forms
from .models import Job, Department
from django import forms
from django.forms import CheckboxSelectMultiple


class JobFilter(django_filters.FilterSet):
    business_title = django_filters.CharFilter(
        field_name="business_title", lookup_expr="icontains", label="Job Title"
    )
    #department_name = django_filters.CharFilter(field_name="department__name", lookup_expr="icontains", label="Department")
    department = django_filters.ModelMultipleChoiceFilter(queryset=Department.objects.all(),
                                                      widget=select2_forms.Select2MultipleWidget())

    work_location = django_filters.CharFilter(field_name="work_location", lookup_expr="icontains", label="Location")
    posting_date = django_filters.DateFromToRangeFilter(
        field_name="posting_date", label="Posted (Between)"
    )
    job_description = django_filters.CharFilter(field_name="job_description", lookup_expr="icontains", label="Description")


    class Meta:
        model = Job
        fields = ["business_title", "work_location",  "posting_date", "department", "job_description"]