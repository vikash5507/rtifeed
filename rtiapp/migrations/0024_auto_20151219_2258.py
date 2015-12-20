# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0023_rti_query_proposed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rti_query',
            name='rti_file_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
    ]
