# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 10:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nin2newslab', '0003_userchoice_select'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userchoice',
            old_name='select',
            new_name='chosen',
        ),
    ]
