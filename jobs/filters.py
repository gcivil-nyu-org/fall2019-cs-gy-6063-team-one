import django_filters
from .models import Job, Department


class JobFilter(django_filters.FilterSet):
    business_title = django_filters.CharFilter(
        field_name="business_title", lookup_expr="icontains", label="Job Title"
    )
    department = django_filters.ModelMultipleChoiceFilter(
        queryset=Department.objects.all()
    )
    work_location = django_filters.CharFilter(
        field_name="work_location", lookup_expr="icontains", label="Location"
    )
    posting_date = django_filters.DateFromToRangeFilter(
        field_name="posting_date", label="Posted (Between)"
    )
    job_description = django_filters.CharFilter(
        field_name="job_description", lookup_expr="icontains", label="Description"
    )

    class Meta:
        model = Job
        fields = [
            "business_title",
            "work_location",
            "posting_date",
            "department",
            "job_description",
        ]
