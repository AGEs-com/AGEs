# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('category_name', models.CharField(max_length=64, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('item_name', models.CharField(max_length=128, unique=True)),
                ('num_of_pictures', models.IntegerField(default=0)),
                ('category', models.ForeignKey(to='AGEs.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('picture_name', models.CharField(max_length=128)),
                ('register_date', models.DateField(default=datetime.datetime.now)),
                ('age', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='picture')),
                ('item', models.ForeignKey(to='AGEs.Item')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
