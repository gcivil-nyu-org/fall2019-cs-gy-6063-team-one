from django.urls import path

from .views import dashboard, ApplicationList

app_name = "dashboard"

urlpatterns = [
    path("", dashboard, name="dashboard"),
    path("<str:app_status>", ApplicationList.as_view(), name="dashboard"),
]
