# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-02 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hys_operation', '0009_auto_20170601_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machineinfo',
            name='os_mark',
            field=models.TextField(max_length=600, null=True, verbose_name='备注'),
        ),
    ]
