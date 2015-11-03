# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0007_auto_20151031_1326'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='authentication_code',
        ),
        migrations.RemoveField(
            model_name='user_profile',
            name='session_code',
        ),
        migrations.AddField(
            model_name='user_profile',
            name='verification_url',
            field=models.CharField(max_length=500, null=True),
            preserve_default=True,
        ),
    ]
