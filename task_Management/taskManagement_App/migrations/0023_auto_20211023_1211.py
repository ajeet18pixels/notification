# Generated by Django 3.2.8 on 2021-10-23 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagement_App', '0022_alter_task_management_task_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='task_management',
            name='created_by_user_email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='task_management',
            name='created_by',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
