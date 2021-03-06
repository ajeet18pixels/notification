# Generated by Django 3.2.8 on 2021-12-29 07:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taskManagement_App', '0085_project_management_project_status_force_update'),
    ]

    operations = [
        migrations.CreateModel(
            name='file_management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_title', models.CharField(max_length=150)),
                ('file_type', models.CharField(max_length=30)),
                ('file', models.FileField(upload_to='Upload_Images/file_management/projectFiles/')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('projectFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskManagement_App.project_management')),
                ('userFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
