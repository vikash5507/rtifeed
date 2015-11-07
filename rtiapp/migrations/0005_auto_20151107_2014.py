# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0004_auto_20151107_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_activity',
            name='user',
        ),
        migrations.DeleteModel(
            name='User_activity',
        ),
    ]
