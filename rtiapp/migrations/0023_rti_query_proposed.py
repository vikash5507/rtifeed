# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0022_auto_20151215_1015'),
    ]

    operations = [
        migrations.AddField(
            model_name='rti_query',
            name='proposed',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
