# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rtiapp', '0041_remove_user_profile_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='num_views',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
