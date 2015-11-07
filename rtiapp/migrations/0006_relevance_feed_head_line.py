# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0005_auto_20151107_2014'),
    ]

    operations = [
        migrations.AddField(
            model_name='relevance',
            name='feed_head_line',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
    ]
