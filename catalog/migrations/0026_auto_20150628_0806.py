# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0025_order_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='goods',
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
