# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0039_blog_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='is_blogger',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
