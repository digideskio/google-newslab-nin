# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-28 20:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nin2newslab', '0035_delete_result'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='option',
        ),
    ]