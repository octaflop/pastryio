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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=254, verbose_name='Name')),
                ('calories', models.IntegerField(blank=True, verbose_name='Calories')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='Photo')),
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
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('step', models.PositiveIntegerField(verbose_name='Step')),
                ('description', models.TextField(verbose_name='Description')),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='Photo')),
                ('recipe', models.ForeignKey(to='recipes.Recipe')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
