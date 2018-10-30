# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-30 10:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0020_restaurant_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='slug',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=b''),
        ),
    ]
