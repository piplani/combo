# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-23 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='lowerlimit',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='data',
            name='upperlimit',
            field=models.IntegerField(default=0),
        ),
    ]
