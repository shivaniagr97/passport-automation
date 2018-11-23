# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-11-23 10:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('pin_code', models.CharField(max_length=6, null=True)),
                ('contact_number', models.CharField(max_length=20, null=True)),
                ('email_id', models.EmailField(max_length=254)),
                ('date_of_joining', models.DateField(null=True)),
            ],
        ),
    ]
