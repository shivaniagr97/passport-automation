# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-24 03:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admins', '0005_auto_20181123_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocsVerified',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_number', models.CharField(max_length=120, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='dates',
            name='from_date',
            field=models.DateField(default=datetime.datetime(2018, 11, 24, 8, 55, 38, 691000)),
        ),
        migrations.AlterField(
            model_name='dates',
            name='to_date',
            field=models.DateField(default=datetime.datetime(2018, 11, 24, 8, 55, 38, 691000)),
        ),
    ]
