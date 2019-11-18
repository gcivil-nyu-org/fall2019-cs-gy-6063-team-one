# Generated by Django 2.2.6 on 2019-11-18 21:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_date', models.DateField(default=datetime.datetime.now)),
                ('status', models.CharField(choices=[('AP', 'Applied'), ('AC', 'Accepted'), ('RE', 'Rejected')], default='AP', max_length=2)),
            ],
        ),
    ]
