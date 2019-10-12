# URLconf - uplyft
from django.urls import path, include
from django.views.generic import TemplateView

# Authentication
from django.contrib.auth import views as auth_views

from . import views

app_name = 'uplyft'
urlpatterns = [
    # ex: /uplyft/
    path('', TemplateView.as_view(template_name="uplyft/index.html"), name='index'),
    # experimental: login with Django stock implementation

    
]
