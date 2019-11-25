# Generated by Django 2.2.6 on 2019-11-24 23:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("uplyft", "0003_auto_20191121_1440")]

    operations = [
        migrations.AlterField(
            model_name="candidateprofile",
            name="cover_letter",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="candidate_cover_letter_directory_path",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["pdf", "doc", "docx"]
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="candidateprofile",
            name="resume",
            field=models.FileField(
                blank=True,
                null=True,
                upload_to="candidate_resume_directory_path",
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["pdf", "doc", "docx"]
                    )
                ],
            ),
        ),
    ]
