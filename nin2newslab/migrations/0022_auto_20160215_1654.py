# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-15 16:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nin2newslab', '0021_problem_html_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TableModal',
            new_name='Modal',
        ),
    ]
