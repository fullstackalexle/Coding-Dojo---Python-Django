# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-02-19 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_shows_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
