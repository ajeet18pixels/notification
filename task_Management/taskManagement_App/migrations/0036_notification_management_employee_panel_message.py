# Generated by Django 3.2.8 on 2021-11-17 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagement_App', '0035_notification_management_notification_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification_management',
            name='employee_panel_message',
            field=models.TextField(blank=True, null=True),
        ),
    ]
