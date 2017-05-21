# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-04-12 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blood_donation', '0003_person_post_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='last_time_donated',
        ),
        migrations.AlterField(
            model_name='person',
            name='contact',
            field=models.DecimalField(decimal_places=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='person',
            name='post_date',
            field=models.DateTimeField(),
        ),
    ]