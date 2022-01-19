# Generated by Django 3.2.8 on 2021-11-29 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagement_App', '0060_auto_20211129_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification_management',
            name='employee_panel_message',
        ),
        migrations.RemoveField(
            model_name='notification_management',
            name='notification_badge_type',
        ),
        migrations.RemoveField(
            model_name='notification_management',
            name='notification_created_by',
        ),
        migrations.RemoveField(
            model_name='notification_management',
            name='notification_created_for',
        ),
        migrations.RemoveField(
            model_name='notification_management',
            name='notification_linked_url',
        ),
        migrations.RemoveField(
            model_name='notification_reciepents',
            name='send_by',
        ),
        migrations.RemoveField(
            model_name='notification_reciepents',
            name='send_to',
        ),
        migrations.AddField(
            model_name='notification_management',
            name='notification_creatives',
            field=models.FileField(blank=True, null=True, upload_to='Upload_Images/notification_Creatives/'),
        ),
        migrations.AddField(
            model_name='notification_management',
            name='notification_sender',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='notification_reciepents',
            name='notification_receiver',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='notification_reciepents',
            name='notificationFK',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='taskManagement_App.notification_management', verbose_name='notificationFK'),
        ),
    ]
