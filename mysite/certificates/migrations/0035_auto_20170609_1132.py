# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-09 18:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0034_auto_20170609_1129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organisedevent',
            old_name='event',
            new_name='organised_event',
        ),
    ]
