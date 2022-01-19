# Generated by Django 3.2.8 on 2021-11-29 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taskManagement_App', '0057_alter_send_bday_anniversary_message_message_send_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='send_bday_anniversary_message',
            name='senderFK',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_fk', to=settings.AUTH_USER_MODEL, verbose_name='sender_FK'),
        ),
    ]