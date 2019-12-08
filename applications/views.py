from django.views.generic import DetailView
from apply.models import Application
from jobs.models import Job
from uplyft.models import Candidate, Employer
from .forms import ProcessApplicationForm
from django.http import HttpResponseForbidden, Http404, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import FormView
from django.views.generic.detail import SingleObjectMixin
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin


class ApplicationDetailView(LoginRequiredMixin, DetailView):
    model = Application
    template_name = "applications/application_detail.html"

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            return HttpResponseRedirect(reverse("errors:not_found"))
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["job"] = Job.objects.get(id=self.get_object().job_id)
        current_user = self.request.user
        application = self.object
        context["forbidden"] = False
        if current_user.is_candidate:
            current_candidate = Candidate.objects.get(user=current_user)
            if application.candidate != current_candidate:
                context["forbidden"] = True
                context["code"] = 403
                context["employer_viewing"] = False
                context["form"] = None
                return context
            context["employer_viewing"] = False
            context["form"] = None

        else:
            current_employer = Employer.objects.get(user=current_user)
            if application.job.department != current_employer.department:
                context["forbidden"] = True
                context["code"] = 403
                context["employer_viewing"] = True
                context["form"] = ProcessApplicationForm()
                return context
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
        return reverse(
            "applications:application_details", kwargs={"pk": self.get_object().pk}
        )


class ProcessApplicationView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = ApplicationDetailView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = ProcessApplication.as_view()
        return view(request, *args, **kwargs)


class WithdrawApplicationView(LoginRequiredMixin, DetailView):
    def post(self, request, *args, **kwargs):
        application = Application.objects.get(id=self.kwargs["pk"])
        if application:
            if application.status == Application.STATUS_APPLIED:
                application.status = Application.STATUS_WITHDRAWN
                application.save()

        """return reverse(
            "applications:application_details", kwargs={"pk": self.kwargs["pk"]}
        )
        """
        return HttpResponseRedirect(
            reverse(
                "applications:application_details", kwargs={"pk": self.kwargs["pk"]}
            )
        )
