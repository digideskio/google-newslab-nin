# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-03 13:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nin2newslab', '0014_logic_max_choice'),
    ]

    operations = [
        migrations.CreateModel(
            name='CountryPay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=10)),
                ('pay', models.IntegerField()),
            ],
        ),
    ]
