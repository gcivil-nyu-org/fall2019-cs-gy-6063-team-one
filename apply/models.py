from django.db import models

MAX_EMAIL_LENGTH = 60

class Application(models.Model):
    job_id = models.IntegerField(primary_key=True)
    email = models.EmailField(max_length=MAX_EMAIL_LENGTH)
    submit_date = models.DateField(null=False, default=datetime.now)

