# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20160721_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='operations',
            field=models.ManyToManyField(through='products.ProductStock', to='products.ManageOperation'),
        ),
    ]
