# Generated by Django 2.1.7 on 2019-06-16 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0018_auto_20190616_0650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='password',
            field=models.CharField(max_length=550),
        ),
    ]
