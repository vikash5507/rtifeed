# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0018_auto_20151207_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_profile',
            name='bio_description',
            field=models.CharField(default=b'', max_length=200),
            preserve_default=True,
        ),
    ]
