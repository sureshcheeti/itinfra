# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-13 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_auto_20190312_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problems',
            name='slot',
            field=models.DateField(default=None, null=True),
        ),
    ]