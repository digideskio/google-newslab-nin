# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-01 06:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nin2newslab', '0005_auto_20160128_1144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nin2Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('explain', models.TextField(default='')),
                ('url', models.CharField(max_length=10)),
            ],
        ),
    ]
