# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0005_auto_20151025_0043'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='email_signed_up',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
