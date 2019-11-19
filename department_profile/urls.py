from django.urls import path

from .views import update_department_profile

app_name = "department_profile"

urlpatterns = [path("", update_department_profile, name="update_department_profile")]
