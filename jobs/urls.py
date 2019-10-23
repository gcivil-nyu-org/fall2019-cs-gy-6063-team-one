from django.urls import path
from . import views

app_name = "jobs"
urlpatterns = [
    # ex: /jobs
    path("dummy_jobs", views.dummy_jobs, name="test_jobs"),
    path("", views.JobsView.as_view(), name="jobs"),
    path("load_jobs", views.load_jobs, name="load_jobs"),
    path("search", views.JobAdvancedSearch.as_view(), name="search"),
    path("results", views.basic_search, name="results")
]
