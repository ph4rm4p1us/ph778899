# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-07 22:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0002_medicinestock_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinestock',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.CoreMedicine'),
        ),
    ]