# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-24 13:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admins', '0007_auto_20181124_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='vstatus',
            name='verification_status',
            field=models.CharField(choices=[('Yes', 'Yes,Verified'), ('No', 'No,Verification Failed')], default='No', max_length=100),
        ),
        migrations.AlterField(
            model_name='dates',
            name='from_date',
            field=models.DateField(default=datetime.datetime(2018, 11, 24, 18, 58, 37, 82000)),
        ),
        migrations.AlterField(
            model_name='dates',
            name='to_date',
            field=models.DateField(default=datetime.datetime(2018, 11, 24, 18, 58, 37, 82000)),
        ),
    ]