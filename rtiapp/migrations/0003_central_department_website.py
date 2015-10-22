# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0002_auto_20151022_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='central_department',
            name='website',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
