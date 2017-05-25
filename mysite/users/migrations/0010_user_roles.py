# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-05-25 10:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20160722_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='roles',
            field=models.CharField(choices=[('F', 'Fencer'), ('C', 'Coach')], default='F', max_length=3),
        ),
    ]
