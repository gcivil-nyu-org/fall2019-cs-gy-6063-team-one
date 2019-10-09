#URLconf - uplyft
from django.urls import path

from . import views

app_name = 'uplyft'
urlpatterns = [
    # ex: /uplyft/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /uplyft/register
    path('register/', views.register, name='register'),
]