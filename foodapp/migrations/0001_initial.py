# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.11.16 on 2018-11-05 20:20
=======
# Generated by Django 1.11.16 on 2018-11-05 19:40
>>>>>>> 22320b5ac8e35d7f3b49350463d79cdd0f411ddb
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('rating', models.IntegerField(blank=True, null=True)),
                ('address', models.CharField(max_length=200)),
                ('website', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('phone_number', models.CharField(blank=True, max_length=200, null=True)),
                ('menu_link', models.CharField(blank=True, default=False, max_length=200)),
                ('lowest_price', models.IntegerField(blank=True, null=True)),
                ('highest_price', models.IntegerField(blank=True, null=True)),
                ('delivery_services', models.BooleanField(default=False)),
                ('student_discounts', models.BooleanField(default=False)),
                ('free_wifi', models.BooleanField(default=False)),
                ('gluten_free_options', models.BooleanField(default=False)),
                ('serves_alcohol', models.BooleanField(default=False)),
                ('vegetarian_options', models.BooleanField(default=False)),
                ('vegan_options', models.BooleanField(default=False)),
                ('twitter_link', models.CharField(blank=True, max_length=200, null=True)),
                ('facebook_link', models.CharField(blank=True, max_length=200, null=True)),
                ('instagram_link', models.CharField(blank=True, max_length=200, null=True)),
                ('monday_hours', models.CharField(blank=True, max_length=200, null=True)),
                ('tuesday_hours', models.CharField(blank=True, max_length=200, null=True)),
                ('wednesday_hours', models.CharField(blank=True, max_length=200, null=True)),
                ('thursday_hours', models.CharField(blank=True, max_length=200, null=True)),
                ('friday_hours', models.CharField(blank=True, max_length=200, null=True)),
                ('saturday_hours', models.CharField(blank=True, max_length=200, null=True)),
                ('sunday_hours', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('rating', models.IntegerField()),
                ('review_text', models.TextField(blank=True, null=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='foodapp.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(choices=[(b'cafe', b'Cafe'), (b'pizza', b'Pizza'), (b'pub', b'Pub'), (b'global', b'Global'), (b'turkish', b'Turkish'), (b'chinese', b'Chinese'), (b'bistro', b'Bistro')], max_length=200)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodapp.Restaurant')),
            ],
        ),
    ]
