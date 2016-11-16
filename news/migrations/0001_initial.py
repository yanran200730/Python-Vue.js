# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('links', models.CharField(max_length=200, verbose_name='新闻链接')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('newsItem', models.CharField(max_length=50, verbose_name='新闻分类')),
                ('article', models.TextField(verbose_name='正文')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.CharField(max_length=50, verbose_name='新闻出处')),
                ('imgs', models.TextField(verbose_name='图片')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
