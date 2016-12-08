# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-08 11:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model_test', '0003_subjecttest'),
    ]

    operations = [
        migrations.AddField(
            model_name='subjecttest',
            name='subject_type',
            field=models.CharField(choices=[('analytical', 'GRE'), ('verbal', 'Verbal')], default='', help_text='Select Subject Type: ', max_length=30),
            preserve_default=False,
        ),
    ]
