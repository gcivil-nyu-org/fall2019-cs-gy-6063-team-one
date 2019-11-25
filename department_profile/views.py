from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse, redirect
from django.utils.translation import gettext as _

from uplyft.decorators import employer_login_required
from uplyft.models import Employer
from .forms import DepartmentProfileForm


@login_required
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
    }

    if request.method == "POST":
        profile_form = DepartmentProfileForm(request.POST, initial=default_data)

        if profile_form.is_valid():
            if profile_form.has_changed():
                updated_profile = profile_form.save()
                department.department_profile = updated_profile
                department.save()
                messages.success(
                    request, _("Department profile was successfully updated")
                )
                return redirect(
                    reverse(
                        "department_details:department_detail",
                        kwargs={"pk": department.id},
                    )
                )
            else:
                messages.error(request, _("No changes requested."))
                return redirect(reverse("department_profile:update_department_profile"))
        else:
            messages.error(request, _("Please correct the error below."))
            return redirect(reverse("department_profile:update_department_profile"))
    else:
        profile_form = DepartmentProfileForm(initial=default_data)
        return render(
            request,
            "department_profile/department_profile.html",
            {"profile_form": profile_form, "department": department},
        )
