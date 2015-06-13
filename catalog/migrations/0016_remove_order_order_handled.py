# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0015_auto_20150608_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_handled',
        ),
    ]
