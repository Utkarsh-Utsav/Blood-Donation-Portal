# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-12 17:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blood_donation', '0002_auto_20170412_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='post_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 4, 12, 17, 22, 7, 936374, tzinfo=utc), verbose_name='date published'),
            preserve_default=False,
        ),
    ]