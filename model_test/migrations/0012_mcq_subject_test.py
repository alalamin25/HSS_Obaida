# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-08 12:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model_test', '0011_remove_mcq_subject_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='mcq',
            name='subject_test',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='model_test.SubjectTest'),
            preserve_default=False,
        ),
    ]
