# Generated by Django 2.2.6 on 2019-11-10 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uplyft', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='uplyft.Candidate')),
                ('candidate_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='uplyft.CandidateProfile')),
            ],
        ),
    ]
