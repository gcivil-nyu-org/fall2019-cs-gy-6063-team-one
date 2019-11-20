
from allauth.account.signals import user_signed_up
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.sites.shortcuts import get_current_site
from django.dispatch import receiver
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.contrib.auth.models import User


from register.token_generator import account_activation_token
from uplyft.models import Candidate, CandidateProfile, Employer, ActiveProfile, CustomUser
from .forms import CandidateRegistrationForm, EmployerRegistrationForm


def candidate_register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("uplyft:index"))
    if request.method == "POST":
        form = CandidateRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=True)
            email = form.cleaned_data.get("email")
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            user.is_candidate = True
            user.is_active = False
            user.save()
            profile = CandidateProfile(
                first_name=first_name, last_name=last_name, email=email
            )
            profile.save()
            candidate = Candidate(user=user, candidate_profile=profile)
            candidate.save()
            active_profile = ActiveProfile(
                candidate=candidate, candidate_profile=profile
            )
            active_profile.save()

            #Send confirmation email to Candidate
            current_site = get_current_site(request)
            email_subject = 'Activate Your Account'
            message = render_to_string('register/activate_account.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(email_subject, message, to=[to_email])
            email.send()
            return render(request, "register/confirmation_message.html")
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
        active_profile = ActiveProfile(candidate=candidate, candidate_profile=profile)
        active_profile.save()

# Activate the account after email confirmation and Login the user.
def activate_account(request, uidb64, token):
    try:
        uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user, "django.contrib.auth.backends.ModelBackend")
        messages.success(request, "Account created successfully")
        return HttpResponseRedirect(reverse("uplyft:index"))
    else:
        return render(request, "register/invalid_activation_link.html")