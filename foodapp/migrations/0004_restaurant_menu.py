# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-28 20:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
        ('foodapp', '0003_auto_20181027_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='menu',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='menu.Menu'),
            preserve_default=False,
        ),
    ]