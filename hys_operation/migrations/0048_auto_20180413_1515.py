# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2018-04-13 07:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hys_operation', '0047_machineinfo_app_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_type_name', models.CharField(max_length=2000, verbose_name='项目归属名称')),
            ],
            options={
                'db_table': 'project_type',
                'verbose_name_plural': 'CO--项目归属',
                'verbose_name': 'CO--项目归属',
            },
        ),
        migrations.AddField(
            model_name='machineinfo',
            name='band_width',
            field=models.ForeignKey(db_column='band_width', default=228, on_delete=django.db.models.deletion.CASCADE, related_name='bandwidth', to='hys_operation.CoDicData', verbose_name='带宽'),
        ),
        migrations.AddField(
            model_name='machineinfo',
            name='mapping_ip',
            field=models.CharField(blank=True, db_column='mapping_ip', max_length=40, null=True, verbose_name='映射ip'),
        ),
        migrations.AlterField(
            model_name='machineinfo',
            name='app_type',
            field=models.CharField(choices=[('WEB', 'WEB'), ('DB', 'DB'), ('虚拟机', '虚拟机')], default='WEB', max_length=8, verbose_name='应用类型'),
        ),
    ]
