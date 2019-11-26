from uplyft.models import (
    CustomUser,
    Candidate,
    Employer,
    CandidateProfile,
    ActiveProfile,
)
from jobs.models import Department
from . import demo_users

# Manage demo candidate users


def create_one_demo_candidates(name_card):
    user = CustomUser.objects.filter(email=name_card["email"])
    if user.count() > 0:
        return

    user = CustomUser.objects.create_user(
        first_name=name_card["first_name"],
        last_name=name_card["last_name"],
        email=name_card["email"],
        password=name_card["password"],
    )
    user.is_candidate = True
    user.is_active = True
    user.save()

    profile = CandidateProfile(
        first_name=name_card["first_name"],
        last_name=name_card["last_name"],
        email=name_card["email"],
    )
    profile.save()

    candidate = Candidate(user=user, candidate_profile=profile)
    candidate.save()

    active_profile = ActiveProfile(candidate=candidate, candidate_profile=profile)
    active_profile.save()


def reset_one_demo_candidate(name_card):
    user = CustomUser.objects.filter(email=name_card["email"])
    if user.count() > 1:
        raise AssertionError()
    if user.count() > 0:
        user.delete()

    create_one_demo_candidates(name_card)


def create_demo_candidates():
    for name_card in demo_users.candidates:
        create_one_demo_candidates(name_card)


def reset_demo_candidates():
    for name_card in demo_users.candidates:
        reset_one_demo_candidate(name_card)


# Manage demo candidate users


def create_one_demo_employer(name_card):
    user = CustomUser.objects.filter(email=name_card["email"])
    if user.count() > 0:
        return

    user = CustomUser.objects.create_user(
        first_name=name_card["first_name"],
        last_name=name_card["last_name"],
        email=name_card["email"],
        password=name_card["password"],
    )
    user.is_candidate = False
    user.is_active = True
    user.save()

    try:
        department = Department.objects.get(name=name_card["department_name"])
    except Department.DoesNotExist:
        department = Department.objects.get(id=name_card["department_id_backup"])

    employer = Employer(user=user, department=department)
    employer.save()


def reset_one_demo_employer(name_card):
    user = CustomUser.objects.filter(email=name_card["email"])
    if user.count() > 1:
        raise AssertionError()
    if user.count() > 0:
        user.delete()

    create_one_demo_employer(name_card)


def create_demo_employers():
    for name_card in demo_users.employers:
        create_one_demo_employer(name_card)


def reset_demo_employers():
    for name_card in demo_users.employers:
        reset_one_demo_employer(name_card)
