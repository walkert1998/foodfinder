# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-10-31 20:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='delivery_services',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='facebook_link',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='free_wifi',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='friday_hours',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='gluten_free_options',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='highest_price',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='image',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='instagram_link',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='lowest_price',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='menu_link',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='monday_hours',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='saturday_hours',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='serves_alcohol',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='student_discounts',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='sunday_hours',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='thursday_hours',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='tuesday_hours',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='twitter_link',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='vegan_options',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='vegetarian_options',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='website',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='wednesday_hours',
        ),
    ]
