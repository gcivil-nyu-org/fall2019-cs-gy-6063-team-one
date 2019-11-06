from django.views.generic import DetailView
from apply.models import Application
from jobs.models import Job
from .forms import ProcessApplicationForm
from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin


class ApplicationDetailView(LoginRequiredMixin, DetailView):
    model = Application
    template_name = "applications/application_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["job"] = Job.objects.get(id=self.get_object().job_id)
        email = self.request.session["email"]
        current_user = get_user_model().objects.get(email=email)
        if current_user.is_candidate:
            context["employer_viewing"] = False
            context["form"] = None
        else:
            context["employer_viewing"] = True
            context["form"] = ProcessApplicationForm()

        return context


class ProcessApplication(SingleObjectMixin, FormView):
    template_name = "applications/application_detail.html"
    form_class = ProcessApplicationForm
    model = Application

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        application = Application.objects.get(id=self.get_object().id)
        if "accept_button" in self.request.POST:
            application.status = "AC"
        elif "reject_button" in self.request.POST:
            application.status = "RE"
        application.save()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        print(self.get_object().pk)
        return reverse(
            "applications:application_details", kwargs={"pk": self.get_object().pk}
        )


class ProcessApplicationView(View):
    def get(self, request, *args, **kwargs):
        view = ApplicationDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ProcessApplication.as_view()
        return view(request, *args, **kwargs)
