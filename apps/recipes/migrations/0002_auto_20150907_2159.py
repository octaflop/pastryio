# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='b36id',
            field=models.CharField(unique=True, max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='b36id',
            field=models.CharField(unique=True, max_length=254, blank=True),
        ),
        migrations.AddField(
            model_name='recipestep',
            name='b36id',
            field=models.CharField(unique=True, max_length=254, blank=True),
        ),
    ]
