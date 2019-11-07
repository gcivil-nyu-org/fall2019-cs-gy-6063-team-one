from django.urls import path

from . import views

app_name = "applications"
urlpatterns = [
    # ex: /applications
    path("<int:pk>", views.ProcessApplicationView.as_view(), name="application_details")
]
