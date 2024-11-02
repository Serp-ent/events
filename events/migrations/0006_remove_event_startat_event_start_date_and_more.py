# Generated by Django 5.1.2 on 2024-11-01 20:09

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_event_participant_limit_eventregistration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='startAt',
        ),
        migrations.AddField(
            model_name='event',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]