# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-10-23 22:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_auto_20181021_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2018, 10, 24, 3, 42, 23, 846127)),
        ),
    ]
