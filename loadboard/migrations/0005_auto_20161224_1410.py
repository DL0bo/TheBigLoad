# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-24 19:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loadboard', '0004_auto_20161218_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loadboard_table',
            name='Company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loadboard.Company_table'),
        ),
    ]
