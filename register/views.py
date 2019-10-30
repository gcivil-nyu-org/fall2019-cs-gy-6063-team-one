from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import CandidateRegistrationForm


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("uplyft:index"))
    if request.method == "POST":
        form = CandidateRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password1")
            user.save()
            user = authenticate(email=email, password=password)
            login(request, user)
            messages.success(request, "Account created successfully")
            return HttpResponseRedirect(reverse("candidate_login:candidate_login"))

    else:
        form = CandidateRegistrationForm()
    return render(request, "register/register.html", {"form": form})
