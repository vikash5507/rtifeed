# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0008_auto_20151031_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='profile_status',
            field=models.CharField(default=b'incomplete', max_length=200),
            preserve_default=True,
        ),
    ]
