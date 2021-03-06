# Generated by Django 3.2.8 on 2021-12-08 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagement_App', '0071_auto_20211208_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_bday_annivarsary_management',
            name='cultural_event_manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cultural_event_manager', to='taskManagement_App.employeedetails', verbose_name='cultural_event_manager'),
        ),
        migrations.AlterField(
            model_name='event_bday_annivarsary_management',
            name='employeeFK',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employeeFK', to='taskManagement_App.employeedetails', verbose_name='employee_FK'),
        ),
    ]
