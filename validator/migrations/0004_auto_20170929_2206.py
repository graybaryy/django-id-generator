# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('validator', '0003_auto_20170929_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='date_of_birth',
            field=models.DateField(default='%m/%d/%y'),
        ),
    ]