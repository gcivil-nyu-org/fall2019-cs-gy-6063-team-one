from django.urls import path

from .views import bad_request, forbidden, internal_error, not_found

app_name = "errors"

urlpatterns = [
    path("forbidden", forbidden, name="forbidden"),
    path("not_found", not_found, name="not_found"),
    path("internal_error", internal_error, name="internal_error"),
    path("bad_request", bad_request, name="bad_request"),
]
