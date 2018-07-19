# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-19 20:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=50)),
                ('description', models.TextField(blank=True, default=None, max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name='Reference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=50)),
                ('description', models.TextField(blank=True, default=None, max_length=2500)),
                ('url', models.CharField(blank=True, default=None, max_length=250)),
                ('category', models.ManyToManyField(blank=True, to='catalogue.Category')),
            ],
        ),
    ]
