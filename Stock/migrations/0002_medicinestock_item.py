# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 22:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0003_auto_20170507_2204'),
        ('Stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicinestock',
            name='item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Core.CoreMedicine'),
        ),
    ]
