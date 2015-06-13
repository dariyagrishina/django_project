# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20150603_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='name_lowercase',
            field=models.CharField(default='a', max_length=200),
            preserve_default=False,
        ),
    ]
