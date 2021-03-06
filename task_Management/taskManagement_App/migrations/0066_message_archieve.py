# Generated by Django 3.2.8 on 2021-12-08 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagement_App', '0065_alter_job_application_resume_doc'),
    ]

    operations = [
        migrations.CreateModel(
            name='message_archieve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('applicationFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskManagement_App.job_application', verbose_name='applicationFK')),
            ],
        ),
    ]
