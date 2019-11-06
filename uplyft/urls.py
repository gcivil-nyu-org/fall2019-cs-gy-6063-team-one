from django.urls import path

from .views import index

app_name = "uplyft"
urlpatterns = [path("", index, name="index")]
