from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


class EmployerLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()

    def confirm_login_allowed(self, user):
        """
        Controls whether the given User may log in. This is a policy setting,
        independent of end-user authentication. This default behavior is to
        allow login by active users, and reject login by inactive users.

        If the given user cannot log in, this method should raise a
        ``forms.ValidationError``.

        If the user is not an Employer, this method should raise a forms.ValidationError

        If the given user may log in, this method should return None.
        """
        if not user.is_active:
            raise forms.ValidationError(
                self.error_messages['inactive'],
                code='inactive',
            )

        if not user.is_employer:
            raise forms.ValidationError(
                "You must be an employer to login this way. Are you a Candidate?"
            )
