# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
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
    ]
