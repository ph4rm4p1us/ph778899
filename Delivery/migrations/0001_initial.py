# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-07 20:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Sales', '0002_auto_20170507_2204'),
        ('Core', '0003_auto_20170507_2204'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryEmployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.Employees')),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryInvoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipped_at', models.DateTimeField()),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sales.SalesInvoice')),
                ('shipped_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.ClientAddress')),
                ('shipped_with', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Delivery.DeliveryEmployee')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_fees', models.FloatField()),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.Area')),
                ('pharmacy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.Pharmacy')),
            ],
        ),
        migrations.AddField(
            model_name='deliveryinvoices',
            name='shipping_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Delivery.ShippingArea'),
        ),
    ]
