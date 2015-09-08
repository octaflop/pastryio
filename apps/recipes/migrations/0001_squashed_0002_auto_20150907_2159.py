# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    replaces = [('recipes', '0001_initial'), ('recipes', '0002_auto_20150907_2159')]

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True, blank=True)),
                ('name', models.CharField(verbose_name='Name', max_length=254)),
                ('calories', models.IntegerField(verbose_name='Calories', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True, blank=True)),
                ('title', models.CharField(verbose_name='Title', max_length=254)),
                ('photo', models.ImageField(verbose_name='Photo', blank=True, upload_to='')),
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
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(null=True, blank=True)),
                ('step', models.PositiveIntegerField(verbose_name='Step')),
                ('description', models.TextField(verbose_name='Description')),
                ('photo', models.ImageField(verbose_name='Photo', blank=True, upload_to='')),
                ('recipe', models.ForeignKey(to='recipes.Recipe')),
                ('b36id', models.CharField(unique=True, blank=True, max_length=254)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='ingredient',
            name='b36id',
            field=models.CharField(unique=True, blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='recipe',
            name='b36id',
            field=models.CharField(unique=True, blank=True, max_length=254),
        ),
    ]
