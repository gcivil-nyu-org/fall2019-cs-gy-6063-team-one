# URLconf - uplyft
from django.urls import path, include
from django.views.generic import TemplateView

# Authentication
from django.contrib.auth import views as auth_views

from . import views

app_name = 'register'
urlpatterns = [
    # ex: /uplyft/register
    path('', views.register, name='register'),
]
