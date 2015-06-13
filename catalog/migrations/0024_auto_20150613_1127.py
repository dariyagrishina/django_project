# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0023_auto_20150612_1715'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OrderView',
            new_name='Order',
        ),
    ]
