# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-11-23 07:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0019_auto_20181123_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(2018, 11, 23, 12, 53, 42, 921043)),
        ),
        migrations.AlterField(
            model_name='documents',
            name='aadhar_card',
            field=models.FileField(blank=True, null=True, upload_to='Documents/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='address_proof',
            field=models.FileField(blank=True, null=True, upload_to='Documents/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='documents',
            name='birth_certificate_or_matric_marksheet',
            field=models.FileField(blank=True, null=True, upload_to='Documents/%Y/%m/%d/'),
        ),
    ]
