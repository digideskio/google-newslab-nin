# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-10 00:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nin2newslab', '0017_auto_20160210_0025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablemodal',
            name='modal_id',
            field=models.CharField(max_length=15),
        ),
    ]