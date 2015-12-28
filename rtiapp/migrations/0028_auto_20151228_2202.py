# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0027_department_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='slug',
            field=models.SlugField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='rti_query',
            name='slug',
            field=models.SlugField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='state',
            name='slug',
            field=models.SlugField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(null=True),
            preserve_default=True,
        ),
    ]
