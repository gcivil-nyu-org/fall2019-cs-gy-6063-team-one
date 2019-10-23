from django.db.models.query import QuerySet
from django.test import TestCase
from django.urls import reverse

from jobs.views import JobsView


class JobsViewTest(TestCase):
    q = ""

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/jobs/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_is_accessible_by_name(self):
        response = self.client.get(reverse("jobs:jobs"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("jobs:jobs"))
        self.assertTemplateUsed(response, "uplyft/base.html")
        self.assertTemplateUsed(response, "jobs/jobs.html")

    def test_form_GET_response_renders_correct_template(self):
        response = self.client.get(
            reverse("jobs:jobs"),
            data={
                "q": self.q,
            }
        )
        self.assertTemplateUsed(response, "uplyft/base.html")
        self.assertTemplateUsed(response, "jobs/jobs.html")

    def test_form_GET_response_returns_queryset_in_context(self):
        response = self.client.get(
            reverse("jobs:jobs"),
            data={
                "q": self.q,
            }
        )
        self.assertIsInstance(response.context['jobs'], QuerySet);

    def test_form_GET_response_returns_correct_view_in_context(self):
        response = self.client.get(
            reverse("jobs:jobs"),
            data={
                "q": self.q,
            }
        )
        self.assertIsInstance(response.context['view'], JobsView)

    def test_form_GET_response_returns_a_queryset(self):
        response = self.client.get(
            reverse("jobs:jobs"),
            data={
                "q": self.q,
            }
        )
        self.assertTrue("jobs" in response.context)
        self.assertIsInstance(response.context["jobs"], QuerySet)

    def test_form_GET_response_retains_form_data(self):
        response = self.client.get(
            reverse("jobs:jobs"),
            data={
                "q": "manager",
            }
        )
        self.assertContains(response, "manager")
