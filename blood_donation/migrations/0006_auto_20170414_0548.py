# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-14 00:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_donation', '0005_auto_20170413_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='contact',
            field=models.IntegerField(max_length=10),
        ),
    ]
