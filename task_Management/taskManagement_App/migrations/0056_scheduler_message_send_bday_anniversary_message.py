# Generated by Django 3.2.8 on 2021-11-29 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagement_App', '0055_event_bday_annivarsary_management'),
    ]

    operations = [
        migrations.CreateModel(
            name='send_bday_anniversary_message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_title', models.CharField(blank=True, max_length=255, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('message_send_time', models.DateTimeField(blank=True, null=True)),
                ('creative', models.FileField(blank=True, null=True, upload_to='Upload_Images/creatives/')),
                ('message_status', models.CharField(blank=True, default='send', max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('receiverFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_fk', to='taskManagement_App.employeedetails', verbose_name='employee_FK')),
                ('senderFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_fk', to='taskManagement_App.employeedetails', verbose_name='employee_FK')),
            ],
        ),
        migrations.CreateModel(
            name='scheduler_message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_schedule_time', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('eventFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskManagement_App.send_bday_anniversary_message', verbose_name='event fk')),
            ],
        ),
    ]
