from django.urls import path
from . import views

app_name = 'jobs'
urlpatterns = [
    # ex: /jobs
    path('', views.jobs, name='jobs'),
]
