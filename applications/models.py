from django.db import models

from uplyft.models import Candidate, CandidateProfile


class ActiveApplication(models.Model):
    # This is effectively the same as having a foreign key with unique=True
    # To ensure each ActiveApplication belongs to only one candidate
    # and also that each candidate can have only one Active Application
    candidate = models.OneToOneField(Candidate, on_delete=models.CASCADE)
    candidate_profile = models.ForeignKey(CandidateProfile, on_delete=models.CASCADE)

    def __str__(self):
        string = "User ID: " + str(self.candidate.user_id)
        string += "; Candidate ID: " + str(self.candidate.id)
        string += "; Profile ID: " + str(self.candidate_profile.id)
