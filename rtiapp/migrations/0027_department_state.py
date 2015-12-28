# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0026_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='state',
            field=models.ForeignKey(to='rtiapp.State', null=True),
            preserve_default=True,
        ),
    ]
