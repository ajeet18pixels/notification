# Generated by Django 3.2.8 on 2021-11-29 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagement_App', '0056_scheduler_message_send_bday_anniversary_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='send_bday_anniversary_message',
            name='message_send_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]