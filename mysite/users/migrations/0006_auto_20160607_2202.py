# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-07 20:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_roles'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='roles',
            field=models.CharField(choices=[('Student', 'Studerende'), ('Professor', 'Professor')], default='Student', max_length=1),
        ),
    ]
