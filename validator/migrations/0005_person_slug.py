# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 01:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validator', '0004_auto_20170929_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]