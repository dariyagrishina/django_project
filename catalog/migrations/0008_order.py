# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_good_name_lowercase'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.IntegerField(max_length=25)),
                ('order_handled', models.BooleanField()),
                ('goods', models.ManyToManyField(to='catalog.Good')),
            ],
        ),
    ]
