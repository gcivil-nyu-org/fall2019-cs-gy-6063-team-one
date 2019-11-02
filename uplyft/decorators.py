from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


# Decorators were incorporated from here:
# https://simpleisbetterthancomplex.com/tutorial/\
# 2018/01/18/how-to-implement-multiple-user-types-with-django.html


def candidate_login_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='candidate_login'):
    """
        Decorator for views that checks that the logged in user is a candidate,
        redirects to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_candidate,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def employer_login_required(function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='employer_login'):
    """
    Decorator for views that checks that the logged in user is an employer,
    redirects to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_employer,
        login_url=login_url,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
