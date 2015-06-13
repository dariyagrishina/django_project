# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_auto_20150610_1101'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderView',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=100)),
                ('handle_order', models.CharField(default=b'ONH', max_length=3, choices=[(b'OH', b'\xd0\x97\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7 \xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xb0\xd0\xbd'), (b'ONH', b'\xd0\x97\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7 \xd0\xbd\xd0\xb5 \xd0\xbe\xd0\xb1\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xb0\xd0\xbd')])),
                ('goods', models.ManyToManyField(to='catalog.Good')),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='goods',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
