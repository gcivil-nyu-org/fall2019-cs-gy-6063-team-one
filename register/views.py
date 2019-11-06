from allauth.account.signals import user_signed_up
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from uplyft.models import Candidate, CandidateProfile, Employer
from .forms import CandidateRegistrationForm, EmployerRegistrationForm


def candidate_register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("uplyft:index"))
    if request.method == "POST":
        form = CandidateRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            user.is_candidate = True
            user.save()
            profile = CandidateProfile(
                first_name=first_name, last_name=last_name, email=email
            )
            profile.save()
            candidate = Candidate(user=user, candidate_profile=profile)
            candidate.save()
            user = authenticate(email=email, password=password)
            login(request, user)
            messages.success(request, "Account created successfully")
            return HttpResponseRedirect(reverse("candidate_login:candidate_login"))
    else:
        form = CandidateRegistrationForm()
    return render(request, "register/candidate_register.html", {"form": form})


def employer_register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("uplyft:index"))
    if request.method == "POST":
        form = EmployerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            department = form.cleaned_data.get("department")
            user.is_candidate = False
            user.save()
            employer = Employer(user=user, department=department)
            employer.save()
            user = authenticate(email=email, password=password)
            login(request, user)
            messages.success(request, "Account created successfully")
            return HttpResponseRedirect(reverse("employer_login:employer_login"))

    else:
        form = EmployerRegistrationForm()
    return render(request, "register/employer_register.html", {"form": form})


# Adding user to CandidateProfile and Candidate when login with gmail
@receiver(user_signed_up)
def populate_profile(sociallogin, user, **kwargs):
    if sociallogin.account.provider == "google":
        user.is_candidate = True
        user.save()
        first_name = user.first_name
        last_name = user.last_name
        email = user.email
        profile = CandidateProfile(
            first_name=first_name, last_name=last_name, email=email
        )
        profile.save()
        candidate = Candidate(user=user, candidate_profile=profile)
        candidate.save()
