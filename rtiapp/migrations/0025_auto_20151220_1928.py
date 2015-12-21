# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0024_auto_20151219_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rti_query',
            name='description',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
