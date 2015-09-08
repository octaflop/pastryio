# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseprofile',
            name='b36id',
            field=models.CharField(blank=True, unique=True, max_length=254),
        ),
        migrations.AddField(
            model_name='baseprofile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 9, 8, 15, 54, 54, 335745, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='baseprofile',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='baseprofile',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2015, 9, 8, 15, 55, 9, 558791, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
