# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-20 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gre_practice_test', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gremcq',
            name='question_type',
        ),
        migrations.AddField(
            model_name='gremcq',
            name='mcq_type',
            field=models.CharField(choices=[('comparation', 'Comparison Question'), ('one', 'One Answer Question'), ('multiple', 'Multiple Answer Question'), ('entry', 'Entry Answer Question')], default=1, help_text='Select MCQ Type: ', max_length=30),
            preserve_default=False,
        ),
    ]
