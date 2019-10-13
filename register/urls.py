from django.urls import path

from . import views

app_name = 'register'
urlpatterns = [
    # ex: /register
    path('', views.register, name='register'),
]
