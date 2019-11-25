from django.urls import path

from .views import DepartmentDetails

app_name = "department_details"

urlpatterns = [path("<int:pk>/", DepartmentDetails.as_view(), name="department_detail")]
