# Generated by Django 2.2.6 on 2019-10-09 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uplyft', '0003_delete_candidateregistrationmodel'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='password2',
        ),
    ]
