from django.urls import path
from . import views

app_name = "candidate_profile"
urlpatterns = [
    # ex: /candidate_profile
    path("", views.update_candidate_profile, name="profile"),
]
