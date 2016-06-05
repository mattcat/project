# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 23:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score1', models.IntegerField(blank=True)),
                ('score2', models.IntegerField(blank=True)),
                ('dategame', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('group', models.CharField(max_length=1)),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='Team1',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team1', to='myapp.Team'),
        ),
        migrations.AddField(
            model_name='game',
            name='Team2',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team2', to='myapp.Team'),
        ),
    ]
