# Generated by Django 3.2.8 on 2021-10-27 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagement_App', '0025_task_management_completed_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_management',
            name='project_status',
            field=models.CharField(blank=True, default='Just Created', max_length=50, null=True),
        ),
    ]