# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0016_remove_rti_query_rti_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rti_response',
            name='description',
        ),
    ]
