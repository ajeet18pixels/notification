# Generated by Django 3.2.8 on 2021-10-28 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagement_App', '0028_task_management_delayed_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task_management',
            old_name='delayed_by',
            new_name='delayed_by_diff',
        ),
    ]
