# Generated by Django 2.2.6 on 2019-10-29 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0002_auto_20191027_1850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='application',
            old_name='job_id',
            new_name='job',
        ),
    ]
