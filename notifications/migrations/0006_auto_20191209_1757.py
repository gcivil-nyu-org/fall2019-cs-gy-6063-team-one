# Generated by Django 2.2.6 on 2019-12-09 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("notifications", "0005_auto_20191209_1743")]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="entity_type",
            field=models.CharField(
                choices=[
                    ("ARJ", "Application Rejected"),
                    ("ARV", "Application Reviewed"),
                    ("AAD", "Application Advanced"),
                    ("ARC", "Application Received"),
                ],
                max_length=3,
            ),
        )
    ]
