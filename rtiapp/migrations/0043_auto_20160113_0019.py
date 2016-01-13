# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0042_blog_num_views'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='reputation',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
    ]
