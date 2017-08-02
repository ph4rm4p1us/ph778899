# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 15:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Core', '0007_employees_salary'),
        ('Accounts', '0006_auto_20170802_0547'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('comment', models.CharField(max_length=128)),
                ('date_added', models.DateTimeField()),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Core.Branches')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.ExpenseCategory')),
                ('paid_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]