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

"""
    path(r'^password-change-done/$', 
    	auth_views.password_change_done,
        {'template_name': 'uplyft/password_change_done.html'},
        name='password_change_done'
        ),
    """