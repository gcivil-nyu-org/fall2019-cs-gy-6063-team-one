from django.urls import path

from .views import DepartmentDetailView

app_name = "department_details"

urlpatterns = [
    path("<int:pk>/", DepartmentDetailView.as_view(), name="department_detail")
]
