# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validator', '0006_auto_20170930_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='race',
            field=models.CharField(choices=[('black', 'Black'), ('white', 'White'), ('other', 'Other')], default='white', max_length=8),
        ),
    ]
