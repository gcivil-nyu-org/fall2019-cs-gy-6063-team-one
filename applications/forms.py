from django.db import models
from django import forms


class ProcessApplicationForm(forms.Form):
    STATUS_ACCEPT = "AC"
    STATUS_REJECT = "RE"
    STATUS_CHOICES = [(STATUS_ACCEPT, "Accept"), (STATUS_REJECT, "Reject")]

    status = models.CharField(max_length=2, choices=STATUS_CHOICES)
