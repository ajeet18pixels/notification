# Generated by Django 3.2.8 on 2021-11-17 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagement_App', '0037_notification_management_notification_linked_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification_management',
            name='notification_badge_type',
            field=models.CharField(blank=True, default='text', max_length=20, null=True),
        ),
    ]