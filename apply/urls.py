from django.urls import path

from . import views

app_name = "apply"
urlpatterns = [
    # ex: /apply
    path("", views.apply, name="apply")
]
