from .models import Job
import django_filters


class JobFilter(django_filters.FilterSet):
    business_title = django_filters.CharFilter(lookup_expr="icontains")
    agency = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = Job
        fields = ["business_title", "work_location", "agency"]
