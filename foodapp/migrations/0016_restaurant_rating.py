# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-30 04:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0015_remove_restaurant_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
