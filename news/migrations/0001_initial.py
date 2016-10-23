# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('newsItem', models.CharField(max_length=50, verbose_name='新闻分类')),
                ('article', models.TextField(verbose_name='正文')),
                ('title', models.CharField(max_length=50, verbose_name='标题')),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('users', models.CharField(max_length=50, verbose_name='新闻出处')),
                ('imgs', models.CharField(max_length=10000, verbose_name='图片')),
            ],
        ),
    ]
