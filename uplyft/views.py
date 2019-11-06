from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("dashboard:dashboard"))

    else:
        return render(request, "uplyft/index.html")
