# Generated by Django 3.2.8 on 2021-12-08 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagement_App', '0067_job_application_applicationdata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_application',
            name='applicationData',
            field=models.DateField(blank=True, null=True),
        ),
    ]