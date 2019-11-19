# Generated by Django 2.2.6 on 2019-11-19 18:45

from django.db import migrations, models
import django.db.models.deletion
import jobs.models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20191118_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, max_length=10000, null=True)),
                ('website', models.URLField(blank=True, help_text='Maximum 200 characters', null=True)),
                ('photo_upload', models.ImageField(upload_to=jobs.models.department_photo_directory_path)),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='department_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.DepartmentProfile'),
        ),
    ]
