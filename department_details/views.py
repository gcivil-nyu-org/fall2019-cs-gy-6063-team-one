from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count
from django.template.defaulttags import register
from django.views.generic import ListView

from jobs.models import Department, Job
from uplyft.models import Employer


# Custom filter, needed to retrieve a dictionary item using its key from
# within a django template (not possible using direct dot notation otherwise)
# Ref: https://stackoverflow.com/questions/8000022/django-
# template-how-to-look-up-a-dictionary-value-with-a-variable
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


ALL = "ALL"


class DepartmentDetails(LoginRequiredMixin, ListView):
    model = Job
    paginate_by = 5
    context_object_name = "jobs"
    template_name = "department_details/department_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        department_id = self.kwargs['pk']
        try:
            department = Department.objects.get(id=department_id)
        except Department.DoesNotExist:
            department = None
        if not department:
            context["department"] = None
            return context

        user = self.request.user
        context["department"] = department

        if department.department_profile is None:
            context["contains_profile"] = False
        else:
            context["contains_profile"] = True

        context["my_department"] = False
        if not user.is_candidate and user.is_active:
            employer = Employer.objects.get(user=user)
            if employer:
                if department.id == employer.department.id:
                    context["my_department"] = True
        context["messages"] = None
        return context

    def get_queryset(self):
        if self.request.user.is_active:
            department_id = self.kwargs['pk']
            jobs = Job.objects.filter(department_id=department_id).annotate(
                count=Count('application')).order_by('-count')
            return jobs
        else:
            return None
