# URLconf - uplyft
from django.urls import path, include
from django.views.generic import TemplateView

# Authentication
from django.contrib.auth import views as auth_views

from . import views

app_name = 'login'
urlpatterns = [
    # ex: /login
    path('', views.UplyftCandidateLoginView.as_view(), name='login'),
    path('/confetti/', views.login_confetti, name='confetti'),
]
