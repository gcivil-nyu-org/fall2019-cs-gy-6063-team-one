# Generated by Django 2.2.6 on 2019-12-04 08:26

import django.core.validators
from django.db import migrations, models
import uplyft.models
import uplyft.s3_storage
import uuid_upload_path.storage


class Migration(migrations.Migration):

    dependencies = [("uplyft", "0009_auto_20191204_0325")]

    operations = [
        migrations.AlterField(
            model_name="candidateprofile",
            name="cover_letter",
            field=models.FileField(
                blank=True,
                null=True,
                storage=uplyft.s3_storage.ResumeStorage(),
                upload_to=uuid_upload_path.storage.upload_to,
                validators=[
                    django.core.validators.FileExtensionValidator(
                        allowed_extensions=["pdf", "doc", "docx"]
                    ),
                    uplyft.models.file_size,
                ],
            ),
        )
    ]