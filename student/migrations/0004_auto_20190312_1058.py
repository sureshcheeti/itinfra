# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-12 10:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_auto_20190312_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id_number',
            field=models.CharField(max_length=30),
        ),
    ]
