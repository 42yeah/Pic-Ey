# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-23 02:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_comment_i'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='settings_to_discover',
            field=models.BooleanField(default=False),
        ),
    ]
