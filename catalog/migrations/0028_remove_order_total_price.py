# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0027_auto_20150628_0807'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
    ]
