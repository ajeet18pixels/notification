# Generated by Django 3.2.7 on 2021-10-25 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagement_App', '0023_auto_20211023_1211'),
    ]

    operations = [
        migrations.AddField(
            model_name='task_management',
            name='updated_by',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='task_management',
            name='updated_by_user_email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
