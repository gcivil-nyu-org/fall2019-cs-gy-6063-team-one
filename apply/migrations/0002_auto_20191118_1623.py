# Generated by Django 2.2.6 on 2019-11-18 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("apply", "0001_initial"),
        ("jobs", "0001_initial"),
        ("uplyft", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="application",
            name="candidate",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="uplyft.Candidate"
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="candidate_profile",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="uplyft.CandidateProfile",
            ),
        ),
        migrations.AddField(
            model_name="application",
            name="job",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="jobs.Job"
            ),
        ),
    ]