# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-05 21:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loadboard', '0007_auto_20170304_2133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loadboard_table',
            old_name='CompanyId',
            new_name='CompanyName',
        ),
        migrations.AlterField(
            model_name='loadboard_table',
            name='CompanyName',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loadboard.Company_table'),
        ),
    ]
