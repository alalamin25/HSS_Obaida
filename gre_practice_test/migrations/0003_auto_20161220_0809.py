# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-20 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gre_practice_test', '0002_auto_20161220_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gremcq',
            name='mcq_type',
            field=models.CharField(choices=[('comparation', 'Comparison Question'), ('single', 'One Answer Question'), ('multiple', 'Multiple Answer Question'), ('entry', 'Entry Answer Question')], help_text='Select MCQ Type: ', max_length=30),
        ),
    ]