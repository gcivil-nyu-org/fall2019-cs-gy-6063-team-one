# Generated by Django 2.2.6 on 2019-11-23 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20191120_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='job_id',
        ),
        migrations.RemoveField(
            model_name='job',
            name='posting_type',
        ),
        migrations.AlterField(
            model_name='job',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
