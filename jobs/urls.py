from django.urls import path

from . import views
from .filters import JobFilter

app_name = "jobs"
urlpatterns = [
    # ex: /jobs
    path("", views.JobsView.as_view(), name="jobs"),
    path("load_jobs", views.load_jobs, name="load_jobs"),
    path("search", views.JobAdvancedSearchView.as_view(filterset_class=JobFilter), name="search"),
    path("<int:pk>/", views.JobDetailView.as_view(), name="job_detail"),
    path("<int:pk>/save", views.save_job, name="save_job"),
]
