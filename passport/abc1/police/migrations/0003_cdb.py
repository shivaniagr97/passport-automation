# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-11-24 04:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('police', '0002_pdb_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='cdb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('reason', models.CharField(max_length=300)),
                ('aadhaarcard', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('doa', models.DateField(max_length=20)),
                ('dor', models.DateField(max_length=20)),
            ],
        ),
    ]