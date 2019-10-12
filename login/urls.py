from django.urls import path
from . import views

app_name = 'login'
urlpatterns = [
    # ex: /login
    path('', views.CandidateLoginView.as_view(), name='login'),
    path('confetti/', views.login_confetti, name='confetti'),
]
