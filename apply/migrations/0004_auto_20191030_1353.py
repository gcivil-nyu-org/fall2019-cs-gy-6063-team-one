# Generated by Django 2.2.6 on 2019-10-30 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("apply", "0003_auto_20191028_2305")]

    operations = [
        migrations.AlterField(
            model_name="application",
            name="status",
            field=models.CharField(
                choices=[("ACTIVE", "ACTIVE"), ("INACTIVE", "INACTIVE")],
                default="ACTIVE",
                max_length=10,
            ),
        )
    ]
