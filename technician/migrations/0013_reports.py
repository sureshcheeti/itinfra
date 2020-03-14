# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-07-01 05:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technician', '0012_delete_stock'),
    ]

    operations = [
        migrations.CreateModel(
            name='reports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_students', models.IntegerField()),
                ('class_room', models.CharField(max_length=30)),
                ('dept', models.CharField(max_length=30)),
                ('block', models.CharField(max_length=30)),
                ('amplifier', models.CharField(max_length=30)),
                ('speakers', models.CharField(max_length=30)),
                ('audio_port', models.CharField(max_length=30)),
                ('audio_cable', models.CharField(max_length=30)),
                ('projector', models.CharField(max_length=30)),
                ('screen', models.CharField(max_length=30)),
                ('video_cable', models.CharField(max_length=30)),
                ('vga_port', models.CharField(max_length=30)),
                ('io_port_not_working_positions', models.CharField(max_length=150)),
                ('how_many_lan_cables_not_working', models.CharField(max_length=150)),
                ('issued_lan_cables', models.IntegerField()),
                ('class_room_ip', models.CharField(max_length=100)),
                ('switch', models.CharField(max_length=30)),
                ('rack', models.CharField(max_length=30)),
                ('adapters_not_working', models.CharField(max_length=150)),
                ('adapters_working', models.CharField(max_length=150)),
                ('screen_damage', models.CharField(max_length=50)),
                ('d_link_modem', models.CharField(max_length=30)),
                ('jio_modem', models.CharField(max_length=30)),
                ('bio_metric_essl_not_registered', models.CharField(max_length=200)),
                ('bio_metric_aadhar_not_registered', models.CharField(max_length=200)),
                ('bio_metric_problems_if_any', models.CharField(max_length=200)),
            ],
        ),
    ]
