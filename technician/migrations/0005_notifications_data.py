# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-13 15:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technician', '0004_auto_20190313_1430'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifications',
            name='data',
            field=models.CharField(default='added', max_length=40),
        ),
    ]
