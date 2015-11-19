# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0009_auto_20151119_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='meta_data',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
