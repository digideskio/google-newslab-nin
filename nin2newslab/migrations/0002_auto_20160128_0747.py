# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-28 07:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('nin2newslab', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userchoice',
            name='user_id',
            field=models.TextField(default=datetime.datetime(2016, 1, 28, 7, 47, 31, 559960, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userchoice',
            name='age',
            field=models.IntegerField(default=20),
        ),
    ]