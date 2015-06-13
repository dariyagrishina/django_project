# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20150603_1052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='goods',
        ),
        migrations.AddField(
            model_name='good',
            name='tags',
            field=models.ManyToManyField(to='catalog.Tag'),
        ),
    ]
