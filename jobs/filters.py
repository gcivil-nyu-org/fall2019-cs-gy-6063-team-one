from .models import Job
import django_filters


class JobFilter(django_filters.FilterSet):
    business_title = django_filters.CharFilter(
        lookup_expr="icontains", label="Job Title"
    )
    agency = django_filters.CharFilter(lookup_expr="icontains", label="Agency")
    work_location = django_filters.CharFilter(lookup_expr="icontains", label="Location")
    posting_date = django_filters.DateFromToRangeFilter(
        field_name="posting_date", label="Posted (Between)"
    )

    class Meta:
        model = Job
        fields = ["business_title", "work_location", "agency", "posting_date"]
