# Generated by Django 3.2.8 on 2021-11-17 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagement_App', '0038_notification_management_notification_badge_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification_management',
            name='notification_created_by',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='notification_management',
            name='notification_created_for',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
