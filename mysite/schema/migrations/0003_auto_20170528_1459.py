# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-28 14:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schema', '0002_auto_20170528_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slotfield',
            name='owner',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
