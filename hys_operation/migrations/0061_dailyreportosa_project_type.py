# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-04-16 03:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hys_operation', '0060_dailyreportosa_machine_room_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailyreportosa',
            name='project_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hys_operation.ProjectType', verbose_name='项目'),
        ),
    ]
