from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView
from django.template.defaulttags import register

from apply.models import Application
from jobs.models import Department, Job


# Custom filter, needed to retrieve a dictionary item using its key from
# within a django template (not possible using direct dot notation otherwise)
# Ref: https://stackoverflow.com/questions/8000022/django-
# template-how-to-look-up-a-dictionary-value-with-a-variable
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


class DepartmentDetailView(LoginRequiredMixin, DetailView):
    model = Department
    template_name = "department_details/department_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        department = self.object
        user = self.request.user
        context["user"] = user
        context["department"] = department

        if department.department_profile is None:
            context["contains_profile"] = False
        else:
            context["contains_profile"] = True

        context["messages"] = None

        jobs = Job.objects.filter(department=department).order_by("-posting_date")
        context["submitted_applications_data"] = {}
        context["jobs"] = jobs
        for job in jobs:
            context["submitted_applications_data"][job.id] = Application.objects.filter(
                job=job
            ).count()

        return context
