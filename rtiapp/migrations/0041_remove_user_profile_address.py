# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0040_user_profile_is_blogger'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_profile',
            name='address',
        ),
    ]
