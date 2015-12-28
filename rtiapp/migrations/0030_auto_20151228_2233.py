# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0029_auto_20151228_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='slug',
            field=models.SlugField(max_length=500, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(max_length=500, null=True),
            preserve_default=True,
        ),
    ]
