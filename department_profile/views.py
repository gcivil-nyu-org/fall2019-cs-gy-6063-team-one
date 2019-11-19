from django.shortcuts import render, reverse, redirect
from django.utils.translation import gettext as _
from uplyft.decorators import employer_login_required
from django.contrib import messages
from .forms import DepartmentProfileForm
from uplyft.models import Employer


@employer_login_required
def update_department_profile(request):
    employer = Employer.objects.get(user=request.user)
    department = employer.department

    default_data = {
        "address": department.department_profile.address
        if department.department_profile is not None
        else None,
        "description": department.department_profile.description
        if department.department_profile is not None
        else None,
        "website": department.department_profile.website
        if department.department_profile is not None
        else None,
        "photo_upload": department.department_profile.photo_upload
        if department.department_profile is not None
        else None,
    }

    if request.method == "POST":
        profile_form = DepartmentProfileForm(request.POST)
        if profile_form.is_valid():
            updated_profile = profile_form.save()
            department.department_profile = updated_profile
            department.save()
            messages.success(request, _("Department profile was successfully updated"))
            return redirect(
                reverse(
                    "department_details:department_detail",
                    kwargs={"pk": department.id},
                )
            )
        else:
            messages.error(request, _("Please correct the error below."))
    else:
        profile_form = DepartmentProfileForm(default_data)
        return render(
            request,
            "department_profile/department_profile.html",
            {"profile_form": profile_form, "department": department},
        )
