# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-20 02:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_prono'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='prono',
            unique_together=set([('user', 'game')]),
        ),
    ]
