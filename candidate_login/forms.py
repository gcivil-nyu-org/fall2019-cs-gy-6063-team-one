from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm


class CandidateLoginForm(AuthenticationForm):
    class Meta:
        model = get_user_model()
