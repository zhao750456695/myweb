# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2018-02-26 15:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180211_1421'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='img',
            new_name='image',
        ),
    ]
