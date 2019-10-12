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
    path('login/', views.UplyftCandidateLoginView.as_view(), name='login'),
    # path('login/', views.uplyft_candidate_login, name='login'),
    path('login/confetti/', views.login_confetti, name='confetti'),
    #path('accounts/', include('django.contrib.auth.urls')),
    
]
