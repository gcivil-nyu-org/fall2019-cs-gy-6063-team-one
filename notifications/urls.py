from django.urls import path

from . import views

app_name = "notifications"
urlpatterns = [
    # ex: /notifications
    path("", views.NotificationCenterView.as_view(), name="notification_center"),
    path("readall", views.read_all, name="readall"),
]
