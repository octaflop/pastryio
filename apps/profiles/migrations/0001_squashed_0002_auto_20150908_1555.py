# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    replaces = [('profiles', '0001_initial'), ('profiles', '0002_auto_20150908_1555')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseProfile',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('avatar', models.ImageField(blank=True, upload_to='', verbose_name='avatar')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('b36id', models.CharField(unique=True, blank=True, max_length=254)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2015, 9, 8, 15, 54, 54, 335745, tzinfo=utc), auto_now_add=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2015, 9, 8, 15, 55, 9, 558791, tzinfo=utc), auto_now=True)),
            ],
        ),
    ]
