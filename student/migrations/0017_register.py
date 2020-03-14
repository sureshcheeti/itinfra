# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-05-06 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0016_stock_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_no', models.CharField(max_length=7)),
                ('email', models.CharField(max_length=100)),
                ('mobile', models.BigIntegerField(blank=True, null=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]