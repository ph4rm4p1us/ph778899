# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-19 03:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Purchases', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseitems',
            name='discount',
            field=models.IntegerField(),
        ),
    ]
