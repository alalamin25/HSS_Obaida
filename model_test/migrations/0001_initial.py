# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-08 11:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('exam_type', models.CharField(choices=[('gre', 'GRE'), ('tofel', 'TOFEL'), ('gmat', 'GMAT')], help_text='Select Exam Type: ', max_length=30)),
                ('fee', models.PositiveSmallIntegerField(default=10)),
            ],
        ),
    ]
