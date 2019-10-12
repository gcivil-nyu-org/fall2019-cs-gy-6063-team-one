from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model


class CandidateLoginForm(AuthenticationForm):
    foo = 'hello'

    class Meta:
        model = get_user_model()
