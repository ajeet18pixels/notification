# Generated by Django 3.2.8 on 2021-12-07 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagement_App', '0063_jobs'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobs',
            name='visibility_status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='jobs',
            name='job_description',
            field=models.TextField(),
        ),
        migrations.CreateModel(
            name='job_application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('contact', models.CharField(max_length=15)),
                ('status', models.CharField(default='Applied', max_length=50)),
                ('resume_doc', models.FileField(blank=True, null=True, upload_to='Upload_Files/applicants_resume/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('experienceFK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskManagement_App.experience_master', verbose_name='experienceFK')),
                ('job_FK', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskManagement_App.jobs', verbose_name='job_FK')),
            ],
            options={
                'unique_together': {('job_FK', 'contact')},
            },
        ),
    ]
