from django.urls import path
from . import views

app_name = 'jobs'
urlpatterns = [
    # ex: /jobs
    path('dummy_jobs', views.dummy_jobs, name='test_jobs'),
    path('', views.JobsView.as_view(), name='jobs'),
    path('fake/', views.generate_fake_data, name='generate_fake_data')

]
