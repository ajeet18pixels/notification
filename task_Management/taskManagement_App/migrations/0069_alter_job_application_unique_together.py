# Generated by Django 3.2.8 on 2021-12-08 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagement_App', '0068_alter_job_application_applicationdata'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='job_application',
            unique_together=set(),
        ),
    ]