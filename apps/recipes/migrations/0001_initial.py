# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('b64id', models.CharField(max_length=1023, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(verbose_name='Name', max_length=254)),
                ('calories', models.IntegerField(blank=True, default=0, verbose_name='Calories')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('b64id', models.CharField(max_length=1023, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(verbose_name='Title', max_length=254)),
                ('photo', models.ImageField(blank=True, verbose_name='Photo', upload_to='')),
                ('author', models.ForeignKey(to='profiles.BaseProfile')),
                ('ingredients', models.ManyToManyField(to='recipes.Ingredient')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RecipeStep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('b64id', models.CharField(max_length=1023, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('step', models.PositiveIntegerField(verbose_name='Step')),
                ('description', models.TextField(verbose_name='Description')),
                ('photo', models.ImageField(blank=True, verbose_name='Photo', upload_to='')),
                ('recipe', models.ForeignKey(to='recipes.Recipe')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
