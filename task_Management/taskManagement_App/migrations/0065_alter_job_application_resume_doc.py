# Generated by Django 3.2.8 on 2021-12-07 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagement_App', '0064_auto_20211207_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_application',
            name='resume_doc',
            field=models.FileField(blank=True, null=True, upload_to='Upload_Images/applicants_resume/'),
        ),
    ]