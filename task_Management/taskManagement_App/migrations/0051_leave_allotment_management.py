# Generated by Django 3.2.8 on 2021-11-24 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagement_App', '0050_auto_20211123_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='leave_allotment_management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_days', models.CharField(blank=True, max_length=10, null=True)),
                ('leave_reason', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('employeeFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskManagement_App.employeedetails', verbose_name='employee_FK')),
            ],
        ),
    ]
