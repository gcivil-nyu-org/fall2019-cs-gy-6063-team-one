# Generated by Django 2.2.6 on 2019-11-06 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12000, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_id', models.IntegerField()),
                ('posting_type', models.CharField(max_length=12000)),
                ('business_title', models.CharField(max_length=12000)),
                ('civil_service_title', models.CharField(max_length=12000)),
                ('title_code_no', models.CharField(max_length=12000)),
                ('level', models.CharField(max_length=12000)),
                ('job_category', models.CharField(max_length=12000)),
                ('ft_pt_indicator', models.CharField(max_length=12000)),
                ('salary_start', models.DecimalField(decimal_places=10, max_digits=1000)),
                ('salary_end', models.DecimalField(decimal_places=10, max_digits=1000)),
                ('salary_frequency', models.CharField(max_length=12000)),
                ('work_location', models.CharField(max_length=12000)),
                ('division', models.CharField(max_length=12000)),
                ('job_description', models.CharField(max_length=12000)),
                ('min_qualifications', models.CharField(max_length=12000)),
                ('preferred_skills', models.CharField(max_length=12000)),
                ('additional_info', models.CharField(max_length=12000)),
                ('to_apply', models.CharField(max_length=12000)),
                ('hours_info', models.CharField(max_length=12000)),
                ('secondary_work_location', models.CharField(max_length=12000)),
                ('recruitment_contact', models.CharField(max_length=12000)),
                ('residency_requirement', models.CharField(max_length=12000)),
                ('posting_date', models.DateField(blank=True, null=True)),
                ('post_until', models.DateField(blank=True, null=True)),
                ('posting_updated', models.DateField(blank=True, null=True)),
                ('process_date', models.DateField(blank=True, null=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.Department')),
            ],
        ),
    ]
