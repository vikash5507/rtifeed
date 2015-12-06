# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0015_auto_20151202_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rti_query',
            name='rti_number',
        ),
    ]
