# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-13 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_donation', '0004_auto_20170412_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='blood_group',
            field=models.CharField(choices=[('A+', 'A+'), ('B+', 'B+'), ('AB+', 'AB+'), ('O+', 'O+'), ('A-', 'A-'), ('B-', 'B-'), ('AB-', 'AB-'), ('O-', 'O-')], max_length=3),
        ),
    ]
