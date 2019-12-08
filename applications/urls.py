from django.urls import path

from . import views

app_name = "applications"
urlpatterns = [
    # ex: /applications
    path(
        "<int:pk>", views.ProcessApplicationView.as_view(), name="application_details"
    ),
    path("withdraw/<int:pk>", views.WithdrawApplicationView.as_view(), name="withdraw"),
]
