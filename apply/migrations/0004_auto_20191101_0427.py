# Generated by Django 2.2.6 on 2019-11-01 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("apply", "0003_auto_20191101_0427")]

    operations = [
        migrations.RenameField(
            model_name="application", old_name="porfolio", new_name="porfolio_website"
        )
    ]
