# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('links', models.CharField(verbose_name='新闻链接', max_length=200)),
            ],
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-created']},
        ),
        migrations.RenameField(
            model_name='news',
            old_name='users',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='time',
            new_name='created',
        ),
        migrations.AlterField(
            model_name='news',
            name='imgs',
            field=models.TextField(verbose_name='图片'),
        ),
    ]
