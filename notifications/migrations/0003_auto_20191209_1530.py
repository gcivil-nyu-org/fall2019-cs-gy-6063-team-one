# Generated by Django 2.2.6 on 2019-12-09 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("notifications", "0002_auto_20191209_1512")]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="entity_type",
            field=models.CharField(
                choices=[
                    ("ARJ", "Application Rejected"),
                    ("ARV", "Application Reviewed"),
                    ("AAD", "Application Advanced"),
                ],
                max_length=3,
            ),
        )
    ]
