# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-05 19:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20181204_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='number_of_items',
            field=models.IntegerField(default=0),
        ),
    ]
