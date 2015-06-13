# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from pytils import translit

def slug(apps, schema_editor):
    tag = apps.get_model('catalog', 'Tag')
    for row in tag.objects.all():
        row.slug = translit.slugify(row.title)
        row.save()

class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_tag_slug'),
    ]

    operations = [
        migrations.RunPython(slug),
    ]
