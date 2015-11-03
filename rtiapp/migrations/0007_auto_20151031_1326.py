# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0006_user_profile_email_signed_up'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='authentication_code',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user_profile',
            name='session_code',
            field=models.CharField(max_length=500, null=True),
            preserve_default=True,
        ),
    ]
