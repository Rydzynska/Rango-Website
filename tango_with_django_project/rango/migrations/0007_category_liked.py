# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-24 12:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_category_voters'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='liked',
            field=models.BooleanField(default=False),
        ),
    ]
