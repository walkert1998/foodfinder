# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-30 04:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0012_review_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='highest_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='lowest_price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
