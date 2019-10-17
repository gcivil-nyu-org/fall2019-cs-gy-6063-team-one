from django.urls import path
from django.views.generic import TemplateView

app_name = "uplyft"
urlpatterns = [
    # ex: /uplyft/
    path("", TemplateView.as_view(template_name="uplyft/index.html"), name="index")
]
