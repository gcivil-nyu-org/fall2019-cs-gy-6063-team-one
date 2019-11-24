"""teamone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URL conf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

handler400 = 'errors.views.bad_request'
handler403 = 'errors.views.forbidden'
handler404 = 'errors.views.not_found'
handler500 = 'errors.views.internal_error'

urlpatterns = [
    path("", include("uplyft.urls")),
    path("admin/", admin.site.urls),
    path("register/", include("register.urls")),
    path("jobs/", include("jobs.urls")),
    path("candidate_login/", include("candidate_login.urls")),
    path("candidate_profile/", include("candidate_profile.urls")),
    path("employer_login/", include("employer_login.urls")),
    path("accounts/", include("allauth.urls")),
    path("password_reset/", include("password_reset.urls")),
    path("apply/", include("apply.urls")),
    path("dashboard/", include("dashboard.urls")),
    path("applications/", include("applications.urls")),
    path("department_details/", include("department_details.urls")),
    path("department_profile/", include("department_profile.urls")),
    path("unauthorized/", include("errors.urls")),

]
