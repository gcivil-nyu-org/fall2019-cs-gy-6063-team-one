from django.urls import path
from .views import IndexView

app_name = "uplyft"
urlpatterns = [
    # ex: /uplyft/
    path("", IndexView.as_view(), name="index")
]
