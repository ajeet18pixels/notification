# Generated by Django 3.2.8 on 2021-10-12 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagement_App', '0002_experience_master_passingyear_master_qualification_master'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeedetails',
            name='upload_docs_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employeedetails',
            name='upload_docs_type_2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employeedetails',
            name='upload_docs_type_3',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employeedetails',
            name='upload_docs_type_4',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='employeedetails',
            name='upload_docs_type_5',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
