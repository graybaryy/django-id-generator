# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 01:22
from __future__ import unicode_literals

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('validator', '0007_auto_20171001_0057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]