# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0011_auto_20151120_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='read_status',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
