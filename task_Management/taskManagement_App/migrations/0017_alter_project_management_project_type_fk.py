# Generated by Django 3.2.8 on 2021-10-18 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagement_App', '0016_auto_20211018_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_management',
            name='project_type_fk',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
