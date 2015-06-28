# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0026_auto_20150628_0806'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedGood',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('good', models.ForeignKey(to='catalog.Good')),
                ('order', models.ForeignKey(to='catalog.Order')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='goods',
            field=models.ManyToManyField(to='catalog.Good', through='catalog.OrderedGood'),
        ),
    ]
