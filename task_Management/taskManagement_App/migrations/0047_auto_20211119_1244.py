# Generated by Django 3.2.8 on 2021-11-19 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskManagement_App', '0046_auditentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditentry',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2021-11-21'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='auditentry',
            name='name',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
