# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 00:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_book', '0002_auto_20170629_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='favorite',
            field=models.ManyToManyField(related_name='favorite_quotes', to='my_book.Quote'),
        ),
    ]
