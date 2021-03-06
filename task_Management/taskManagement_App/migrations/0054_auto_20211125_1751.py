# Generated by Django 3.2.8 on 2021-11-25 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagement_App', '0053_auto_20211125_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='event_highlight_Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highlight_name', models.CharField(max_length=100, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='culturalevent_master',
            name='manager_image',
        ),
    ]
