# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-29 11:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0003_auto_20170528_1459'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slotfield',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='slotfield',
            name='slot_id',
        ),
        migrations.AlterField(
            model_name='choice',
            name='slot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schema.SlotField', unique=True),
        ),
    ]