# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-03 06:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('technician', '0007_admin_notify'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin_notify',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
