# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-02-27 03:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_auto_20180227_1124'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='workshift',
        ),
        migrations.RemoveField(
            model_name='post',
            name='workshop',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='Workshift',
        ),
        migrations.DeleteModel(
            name='Workshop',
        ),
    ]
